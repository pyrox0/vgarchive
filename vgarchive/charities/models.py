# ruff:noqa
# type:ignore
from django.db import models
from django.db.models import Sum
from django.urls import reverse


class Charity(models.Model):
    """Represents a charity that can be donated to.

    Attributes:
        id: the ID of the charity, used for URLs
        name: Display name of the charity
        short_name: A shorter display name for some circumstances
        homepage: URL for the charity's homepage
        icon: Icon to display when needed
        founded: The founding year of the charity.
        twitter: Twitter username of the charity.
        youtube: Youtube username of the charity.
        bluesky: Bluesky account of the charity.
    """

    class Meta:
        verbose_name_plural = "Charities"

    id = models.SlugField("ID", primary_key=True, max_length=200)
    name = models.CharField("Display Name", max_length=200)
    short_name = models.CharField("Short Name", max_length=20, blank=True)
    homepage = models.URLField("Charity Homepage", blank=True)
    icon = models.ImageField("Icon/Favicon", blank=True)
    founded = models.IntegerField("Founding Year", default=2024)
    twitter = models.CharField("Twitter Account", max_length=15, blank=True)
    youtube = models.CharField("Youtube Channel", max_length=200, blank=True)
    bluesky = models.CharField("Bluesky Account", max_length=200, blank=True)

    def donation_total(self):
        return self.event_set.aggregate(Sum("donation_total"))["donation_total__sum"]

    def get_absolute_url(self):
        return reverse("charity-detail", args=[self.id])

    def __str__(self) -> str:  # noqa
        return self.name  # type:ignore
