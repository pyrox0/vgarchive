# ruff:noqa
# type:ignore
from pathlib import Path
from django.db import models
from django.db.models import Sum
from django.urls import reverse

from imagekit.models import ProcessedImageField

from vgarchive.validators.bluesky import validate_bluesky

__all__ = ["Organization"]


def _upload_banner(instance, filename):
    return f"org-banners/{Path(filename).with_stem(instance.id)}"


def _upload_icon(instance, filename):
    return f"org-icons/{Path(filename).with_stem(instance.id)}"


class Organization(models.Model):
    id = models.SlugField("ID", primary_key=True, max_length=200)
    name = models.CharField("Name", max_length=100)
    description = models.TextField("Description")
    homepage = models.URLField("Organization Homepage", blank=True)
    icon = ProcessedImageField(
        verbose_name="Favicon/Icon",
        upload_to=_upload_icon,
        format="WEBP",
        options={"quality": 95},
    )
    banner = ProcessedImageField(
        verbose_name="Banner Image",
        upload_to=_upload_banner,
        format="WEBP",
        options={"quality": 95},
    )
    tracker = models.URLField("Donation Tracker", max_length=200, blank=True)
    twitch = models.CharField("Twitch Channel", max_length=25, blank=True)
    twitter = models.CharField("Twitter Username", max_length=15, blank=True)
    youtube = models.CharField("Youtube Channel", max_length=200, blank=True)
    bluesky = models.CharField(
        "Bluesky Account", max_length=200, blank=True, validators=[validate_bluesky]
    )

    def num_donations(self):
        return self.event_set.aggregate(Sum("num_donations"))["num_donations__sum"]

    def donation_total(self):
        return self.event_set.aggregate(Sum("donation_total"))["donation_total__sum"]

    def get_absolute_url(self):
        return reverse("organization-detail", args=[self.id])

    def __str__(self) -> str:
        return self.name
