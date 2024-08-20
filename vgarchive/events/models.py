from django.db import models
from django.db.models import CASCADE
from django.utils.translation import gettext_lazy as _

from ..organizations.models import Organization
from ..charities.models import Charity

# Create your models here.


class Event(models.Model):
    """Represents a marathon event.

    Attributes:
        id: The ID, used for URLs
        marathon_id: The ID of the marathon this event belongs to
        name: The display name of the event
        source: Marks a source that event data was imported from, if available
        homepage: Link to the event's homepage
        schedule: Link to the event's schedule
        donation_total: How much money this event raised
        donations: Link to a page containing this event's donations
        charity_id: The charity that this event raised money for
        youtube_playlist: Youtube Playlist that contains VODs from this event

    """

    class EventSources(models.TextChoices):
        TRACKER = "tracker", _("GDQ Tracker")
        OENGUS = "oengus", _("Oengus")
        MANUAL = "manual", _("Manual Import")

    id = models.CharField("ID", primary_key=True, max_length=200)
    organization = models.ForeignKey(
        Organization, CASCADE, verbose_name="Organization", default="none"
    )
    name = models.CharField("Display Name", max_length=200)
    source = models.CharField(
        "Event Source", max_length=10, choices=EventSources, default=EventSources.MANUAL
    )
    homepage = models.URLField("Event Homepage", blank=True)
    schedule = models.URLField("Schedule Link")
    donation_total = models.DecimalField(
        "Donation Total", max_digits=20, decimal_places=2
    )
    donations = models.URLField("Donations Page", blank=True)
    charity = models.ForeignKey(
        Charity, CASCADE, verbose_name="Supported Charity", default="none"
    )
    youtube_playlist = models.URLField("Youtube VOD Playlist", blank=True)
