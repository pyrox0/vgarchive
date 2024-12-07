from django.db import models
from django.utils.translation import gettext_lazy as _

__all__ = ["DataSources"]


class DataSources(models.TextChoices):
    TRACKER = "tracker", _("GDQ Tracker")
    OENGUS = "oengus", _("Oengus")
    HORARO = "horaro", _("Horaro")
    MANUAL = "manual", _("Manual Import")
