from urllib.parse import urlparse
from django.core.exceptions import ValidationError
from django.utils.html import format_html


def is_twitch_url(value) -> None:  # noqa
    obj = urlparse(value)
    if obj.hostname != "twitch.tv":
        raise ValidationError("Provided link is not a Twitch link!")


def is_youtube_url(value) -> None:  # noqa
    obj = urlparse(value)
    if obj.hostname not in ("youtube.com", "youtu.be", "www.youtube.com"):
        raise ValidationError("Provided link is not a Youtube link!")


def render_homepage(value):  # noqa
    return format_html(
        f'<a class="external-link link-info" href="{value}">Homepage</a>'
    )


def render_twitch(name, value):  # noqa
    return format_html(
        f'<a class="link text-primary" aria-label="{name} Twitch Channel" href="https://twitch.tv/{value}"><i class="bi-twitch text-3xl"></i></a>'
    )


def render_twitter(name, value):  # noqa
    return format_html(
        f'<a class="link text-info" aria-label="{name} Twitter Account" href="https://x.com/{value}"><i class="bi-twitter text-3xl"></i></a>'
    )


def render_youtube(name, value):  # noqa
    return format_html(
        f'<a class="link text-error" aria-label="{name} Youtube Channel" href="https://youtube.com/{value}"><i class="bi-youtube text-3xl"></i></a>'
    )


def render_bluesky(name, value):  # noqa
    return format_html(
        f'<a class="external-link link-info" aria-label="{name} Bluesky Account" href="https://bsky.app/profile/{value}"><i class="bi-square-fill text-3xl"></i></a>'
    )


def render_linkedin(name, value):  # noqa
    return format_html(
        f'<a class="link-info" aria-label="{name} Linkedin Account" href=https://linkedin.com/company/{value}"><i class="bi-linkedin text-3xl"></i></a>'
    )


def render_facebook(name, value):  # noqa
    return format_html(
        f'<a class="link-info" aria-label="{name} Facebook Page" href=https://facebook.com/{value}"><i class="bi-facebook text-3xl"></i></a>'
    )
