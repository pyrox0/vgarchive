# ruff:noqa
# type:ignore
from django.db import models
from django.db.models import Sum
from django.urls import reverse


class Organization(models.Model):
    id = models.SlugField("ID", primary_key=True, max_length=200)
    name = models.CharField("Name", max_length=100)
    description = models.TextField("Description")
    homepage = models.URLField("Organization Homepage", blank=True)
    icon = models.ImageField("Favicon/Icon")
    banner = models.ImageField("Banner Image")
    tracker = models.URLField("Donation Tracker", max_length=200, blank=True)
    twitch = models.CharField("Twitch Channel", max_length=25, blank=True)
    twitter = models.CharField("Twitter Username", max_length=15, blank=True)
    youtube = models.CharField("Youtube Channel", max_length=200, blank=True)
    bluesky = models.CharField("Bluesky Account", max_length=200, blank=True)

    def num_donations(self):
        return self.event_set.aggregate(Sum("num_donations"))["num_donations__sum"]

    def donation_total(self):
        return self.event_set.aggregate(Sum("donation_total"))["donation_total__sum"]

    def get_absolute_url(self):
        return reverse("organization-detail", args=[self.id])

    def __str__(self) -> str:
        return self.name
