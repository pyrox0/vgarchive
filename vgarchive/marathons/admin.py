from django.contrib import admin

from vgarchive.admin import site

from .models import Marathon


@admin.register(Marathon, site=site)
class MarathonAdmin(admin.ModelAdmin):
    pass
