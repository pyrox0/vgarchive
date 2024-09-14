from urllib.parse import urlparse
from django.core.exceptions import ValidationError


def is_twitch_url(value) -> None:  # noqa
    obj = urlparse(value)
    if obj.hostname != "twitch.tv":
        raise ValidationError("Provided link is not a Twitch link!")


def is_youtube_url(value) -> None:  # noqa
    obj = urlparse(value)
    if obj.hostname not in ("youtube.com", "youtu.be", "www.youtube.com"):
        raise ValidationError("Provided link is not a Youtube link!")
