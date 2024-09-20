from django.contrib import admin

from vgarchive.admin import site

from .models import Organization


@admin.register(Organization, site=site)
class OrganizationAdmin(admin.ModelAdmin):
    exclude = ("donation_total", "num_donations")
    fieldsets = (
        (None, {"fields": ["id", "name", "description"]}),
        ("Images", {"fields": ["banner", "icon"]}),
        ("Links", {"fields": ["homepage", "tracker"]}),
        ("Socials", {"fields": ["bluesky", "twitch", "twitter", "youtube"]}),
    )
