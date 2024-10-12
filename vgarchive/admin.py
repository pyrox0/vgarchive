from django.contrib.admin import site
from django.contrib import admin

from .models.charity import Charity

site.site_header = "VGArchive Administration"
site.site_title = "VGArchive Administration"
site.index_title = "Administration"


@admin.register(Charity, site=site)
class CharityAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ["id", "name", "short_name", "homepage", "founded", "icon"]}),
        ("Socials", {"fields": ["bluesky", "twitter", "youtube"]}),
    )
