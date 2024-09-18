from django.contrib import admin

from .models import Run, Runner, Game

from vgarchive.admin import site


@admin.register(Game, site=site)
class GameAdmin(admin.ModelAdmin):
    fields = ("name", "id")
    prepopulated_fields = {"id": ["name"]}  # noqa


@admin.register(Runner, site=site)
class RunnerAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ["name", "pronouns"]}),
        ("Socials", {"fields": ["bluesky", "twitch", "twitter", "youtube"]}),
    )


@admin.register(Run, site=site)
class RunAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": [
                    "game",
                    "category",
                    "platform",
                    "length",
                    "event",
                    "runners",
                    "youtube",
                    "twitch",
                ]
            },
        ),
    )
