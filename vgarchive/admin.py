from django.contrib.admin import site
from django.contrib import admin

from .models.charity import Charity
from .models.event import Event
from .models.organization import Organization


site.site_header = "VGArchive Administration"
site.site_title = "VGArchive Administration"
site.index_title = "Administration"


@admin.register(Charity, site=site)
class CharityAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ["id", "name", "short_name", "homepage", "founded", "icon"]}),
        ("Socials", {"fields": ["bluesky", "twitter", "youtube"]}),
    )


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
            {"fields": ["start_date", "end_date"], "classes": ["collapse"]},
        ),
    )


@admin.register(Organization, site=site)
class OrganizationAdmin(admin.ModelAdmin):
    exclude = ("donation_total", "num_donations")
    fieldsets = (
        (None, {"fields": ["id", "name", "description"]}),
        ("Images", {"fields": ["banner", "icon"]}),
        ("Links", {"fields": ["homepage", "tracker"]}),
        ("Socials", {"fields": ["bluesky", "twitch", "twitter", "youtube"]}),
    )
