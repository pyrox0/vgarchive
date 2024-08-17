from django.db import models

# Create your models here.


class Charity(models.Model):
    """Represents a charity that can be donated to.

    Attributes:
        id: the ID of the charity, used for URLs
        name: Display name of the charity
        homepage: URL for the charity's homepage
    """

    id = models.CharField("ID", primary_key=True, max_length=200)
    name = models.CharField("Display Name", max_length=200)
    homepage = models.URLField("Charity Homepage", blank=True)
    icon = models.ImageField("Icon/Favicon", blank=True)
    founded = models.IntegerField("Founding Year", default=2024)
