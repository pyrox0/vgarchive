from django.contrib import admin

from .models import Run, Runner, Game

from vgarchive.admin import site


@admin.register(Game, site=site)
class GameAdmin(admin.ModelAdmin):
    pass


@admin.register(Runner, site=site)
class RunnerAdmin(admin.ModelAdmin):
    pass


@admin.register(Run, site=site)
class RunAdmin(admin.ModelAdmin):
    pass
