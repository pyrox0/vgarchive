from django.db import models

from vgarchive.events.models import Event


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
        Event,
        models.CASCADE,
        verbose_name="Event",
        default="none",
    )
    game = models.CharField("Game Name", max_length=200)
    category = models.CharField("Category", max_length=200)
    platform = models.CharField("Platform", max_length=200)
    length = models.DurationField("Run Length")
    runners = models.CharField("Runners", max_length=200)
    youtube = models.URLField()
    twitch = models.URLField()

    class Meta:
        db_table_comment = "Runs"

    def __str__(self) -> str:  # noqa
        return f"{self.game} {self.category} at {self.event.name}"
