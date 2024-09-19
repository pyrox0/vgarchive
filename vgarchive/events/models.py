from django.db import models
from django.db.models import CASCADE
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from vgarchive.organizations.models import Organization
from vgarchive.charities.models import Charity


class Event(models.Model):
    """Represents a marathon event.

    Attributes:
        id: The ID, used for URLs
        organization: The ID of the marathon this event belongs to
        name: The display name of the event
        short_name: Shorter version of the event name, if available
        source: Marks a source that event data was imported from, if available
        start_datetime: The date and time of the event starting.
        end_datetime: The ending datetime of the event.
        homepage: Link to the event's homepage
        schedule: Link to the event's schedule
        donation_total: How much money this event raised
        donations: Link to a page containing this event's donations
        num_donations: The number of donations for this event.
        charity: The charity that this event raised money for
        youtube_playlist: Youtube Playlist that contains VODs from this event
        banner: URL to a banner image for the event.

    """

    class EventSources(models.TextChoices):
        TRACKER = "tracker", _("GDQ Tracker")
        OENGUS = "oengus", _("Oengus")
        MANUAL = "manual", _("Manual Import")

    id = models.SlugField("ID", primary_key=True, max_length=200)
    organization = models.ForeignKey(
        Organization,
        CASCADE,
        verbose_name="Organization",
        default="none",
    )
    name = models.CharField("Display Name", max_length=200)
    short_name = models.CharField("Short Name(optional)", max_length=20, blank=True)
    source = models.CharField(
        "Event Source",
        max_length=10,
        choices=EventSources,
        default=EventSources.MANUAL,
    )
    start_datetime = models.DateTimeField("Start Date and Time")
    end_datetime = models.DateTimeField("End Date and Time")
    duration = models.DurationField("Duration")
    homepage = models.URLField("Event Homepage", blank=True)
    schedule = models.URLField("Schedule Link")
    donation_total = models.DecimalField(
        "Donation Total", max_digits=20, decimal_places=2
    )
    donations = models.URLField("Donations Page", blank=True)
    num_donations = models.IntegerField("Number of Donations")
    charity = models.ForeignKey(
        Charity,
        CASCADE,
        verbose_name="Supported Charity",
        default="none",
    )
    youtube_playlist = models.URLField("Youtube VOD Playlist", blank=True)
    banner = models.ImageField("Banner Image", blank=True)

    def get_absolute_url(self):  # noqa
        return reverse("event-detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):  # noqa
        self.duration = self.end_datetime - self.start_datetime  # type:ignore
        super().save(*args, **kwargs)

    def __str__(self) -> str:  # noqa
        return self.name  # type:ignore
