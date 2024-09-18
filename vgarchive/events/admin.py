from django.contrib import admin

from vgarchive.admin import site

from .models import Event

# Register your models here.


@admin.register(Event, site=site)
class EventAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": [
                    "id",
                    "organization",
                    "name",
                    "short_name",
                    "source",
                    "banner",
                ]
            },
        ),
        (
            "Links",
            {"fields": ["homepage", "schedule", "donations", "youtube_playlist"]},
        ),
        ("Donations", {"fields": ["donation_total", "num_donations"]}),
        (
            "Time",
            {"fields": ["start_datetime", "end_datetime"], "classes": ["collapse"]},
        ),
    )
