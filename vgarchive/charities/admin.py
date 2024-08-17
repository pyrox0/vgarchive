from django.contrib import admin

from vgarchive.admin import site

from .models import Charity

# Register your models here.


@admin.register(Charity, site=site)
class CharityAdmin(admin.ModelAdmin):
    pass
