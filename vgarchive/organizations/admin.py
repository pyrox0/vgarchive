from django.contrib import admin

from vgarchive.admin import site

from .models import Organization


@admin.register(Organization, site=site)
class OrganizationAdmin(admin.ModelAdmin):
    pass
