from django.contrib import admin

from vgarchive.admin import site

from .models import Event

# Register your models here.


@admin.register(Event, site=site)
class EventAdmin(admin.ModelAdmin):
    pass
