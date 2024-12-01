from django.views.generic.edit import CreateView

from vgarchive.models.run import Game, Runner, Run
from vgarchive.models.charity import Charity


class CharityIngest(CreateView):
    model = Charity
    fields = (
        "id",
        "name",
        "short_name",
        "homepage",
        "icon",
        "founded",
        "twitter",
        "youtube",
        "bluesky",
    )

    template_name = "vgarchive/forms/charity-ingest.html"


class GameIngest(CreateView):
    model = Game
    fields = ["name"]  # noqa

    template_name = "vgarchive/forms/game-ingest.html"


class RunnerIngest(CreateView):
    model = Runner
    fields = (
        "name",
        "pronouns",
        "twitch",
        "youtube",
        "twitter",
        "bluesky",
    )

    template_name = "vgarchive/forms/runner-ingest.html"


class RunIngest(CreateView):
    model = Run
    success_url = "/runs"
    fields = (
        "game",
        "category",
        "platform",
        "length",
        "event",
        "runners",
        "youtube",
        "twitch",
    )
    template_name = "vgarchive/forms/run-ingest.html"
