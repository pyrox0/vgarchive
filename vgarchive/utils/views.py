from django.utils.html import format_html

import django_tables2 as tables


class BlueskyColumn(tables.Column):
    orderable = False

    def render(self, value, record):  # noqa # type:ignore
        return format_html(
            f'<a class="external-link link-info" aria-label="{record.name} Bluesky Account" href="https://bsky.app/profile/{value}"><i class="bi-square-fill text-3xl"></i></a>'
        )


class TwitchColumn(tables.Column):
    orderable = False

    def render(self, value, record):  # noqa # type:ignore
        return format_html(
            f'<a class="link text-primary" aria-label="{record.name} Twitch Channel" href="https://twitch.tv/{value}"><i class="bi-twitch text-3xl"></i></a>'
        )


class TwitterColumn(tables.Column):
    orderable = False

    def render(self, value, record):  # noqa # type:ignore
        return format_html(
            f'<a class="link text-info" aria-label="{record.name} Twitter Account" href="https://x.com/{value}"><i class="bi-twitter text-3xl"></i></a>'
        )


class YoutubeColumn(tables.Column):
    orderable = False

    def render(self, value, record):  # noqa # type:ignore
        return format_html(
            f'<a class="link text-error" aria-label="{record.name} Youtube Channel" href="https://youtube.com/{value}"><i class="bi-youtube text-3xl"></i></a>'
        )


class HomepageColumn(tables.Column):
    orderable = False

    def render(self, value):  # noqa # type:ignore
        return format_html(
            f'<a class="external-link link-info" href="{value}">Homepage</a>'
        )
