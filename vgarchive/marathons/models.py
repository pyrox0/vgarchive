from django.db import models


class Marathon(models.Model):
    id = models.CharField("ID", primary_key=True, max_length=200)
    name = models.CharField("Title", max_length=100)
    description = models.TextField("Description")
    homepage = models.URLField("Marathon Homepage", blank=True)
    active = models.BooleanField("Is Marathon Active?", default=True)  # type:ignore
    icon = models.ImageField("Favicon/Icon")
    banner = models.ImageField("Banner Image")
    twitch = models.CharField("Twitch Channel", max_length=25, blank=True)
    twitter = models.CharField("Twitter Username", max_length=15, blank=True)
    youtube = models.URLField("Youtube Channel", blank=True)

    class Meta:
        db_table_comment = "Marathons"
