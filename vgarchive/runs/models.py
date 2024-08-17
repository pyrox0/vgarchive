from django.db import models

from ..events.models import Event

# Create your models here.


class Run(models.Model):
    """A run at an event.

    Attributes:
        id: The run's ID
        event: The event the run was performed at
        platform: The platform the game was played on
        game: The name of the game ran
        length: The length of the run
        runners: The runner(s) who performed the run
        youtube: Link to a Youtube VOD of the run
        twitch: Link to a Twitch VOD of the run
    """

    event = models.ForeignKey(
        Event, models.CASCADE, verbose_name="Event", default="none"
    )
    game = models.CharField("Game Name", max_length=200)
    platform = models.CharField("Platform", max_length=200)
    length = models.DurationField("Run Length")
    runners = models.CharField("Runners", max_length=200)
    youtube = models.URLField()
    twitch = models.URLField()

    class Meta:
        db_table_comment = "Runs"
