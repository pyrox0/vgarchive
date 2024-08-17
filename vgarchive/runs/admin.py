from django.contrib import admin

from .models import Run

from vgarchive.admin import site


@admin.register(Run, site=site)
class RunAdmin(admin.ModelAdmin):
    pass
