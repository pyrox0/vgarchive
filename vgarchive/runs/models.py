from typing import Self
from django.db import models

from vgarchive.events.models import Event
from vgarchive.utils import is_youtube_url, is_twitch_url


class Game(models.Model):
    """A game that's been run at an event.

    Attributes:
        id: The game's ID
        name: The game's name

    """

    id = models.CharField(primary_key=True, max_length=200)
    name = models.CharField("Game Name", max_length=200)

    def save(self, *args, **kwargs):  # noqa
        self.id = self.name.lower()  # type:ignore
        super().save(*args, **kwargs)

    def __str__(self) -> str:  # noqa
        return self.name  # type:ignore


class Runner(models.Model):
    """A runner of a game.

    Attributes:
        name: Their name
        pronouns: Their pronouns
        twitch: Their Twitch username, can be null
        youtube: Their Youtube channel, can be null
        twitter: Their Twitter account username, can be null
        bluesky: Their Bluesky account username, can be null
    """

    name = models.CharField("Name", max_length=200)
    pronouns = models.CharField("Pronouns", max_length=50, blank=True)
    twitch = models.CharField("Twitch Channel", max_length=25, blank=True)
    youtube = models.CharField("Youtube Channel", max_length=200, blank=True)
    twitter = models.CharField("Twitter Username", max_length=15, blank=True)
    bluesky = models.CharField("Bluesky Username", max_length=200, blank=True)

    def __str__(self: Self) -> str:
        if self.pronouns:
            return f"{self.name} ({self.pronouns})"

        return f"{self.name}"


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
    game = models.ForeignKey(Game, models.PROTECT, verbose_name="Game")
    category = models.CharField("Category", max_length=200)
    platform = models.CharField("Platform", max_length=200)
    length = models.DurationField("Run Length")
    runners = models.ManyToManyField(Runner, verbose_name="Runners")
    youtube = models.URLField("Youtube VOD Link", validators=[is_youtube_url])
    twitch = models.URLField("Twitch VOD Link", validators=[is_twitch_url], blank=True)

    class Meta:
        db_table_comment = "Runs"

    def __str__(self) -> str:  # noqa
        if self.event.short_name:  # type:ignore
            return f"{self.game} {self.category} at {self.event.short_name}"  # type:ignore
        return f"{self.game} {self.category} at {self.event.name}"
