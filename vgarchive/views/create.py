from django.views.generic.edit import CreateView

from vgarchive.models.charity import Charity
from vgarchive.models.event import Event
from vgarchive.models.organization import Organization
from vgarchive.models.run import Game, Runner, Run

__all__ = [
    "CharityCreate",
    "EventCreate",
    "GameCreate",
    "OrganizationCreate",
    "RunnerCreate",
    "RunCreate",
]


class CharityCreate(CreateView):
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

    template_name = "vgarchive/forms/charity-create.html"


class EventCreate(CreateView):
    model = Event
    fields = (
        "id",
        "name",
        "short_name",
        "start_date",
        "end_date",
        "homepage",
        "schedule",
        "donation_total",
        "donations",
        "num_donations",
        "charity",
        "youtube_playlist",
        "banner",
    )
    template_name = "vgarchive/forms/event-create.html"


class GameCreate(CreateView):
    model = Game
    fields = ["name"]  # noqa

    template_name = "vgarchive/forms/game-create.html"


class OrganizationCreate(CreateView):
    model = Organization
    fields = (
        "id",
        "name",
        "description",
        "homepage",
        "icon",
        "banner",
        "tracker",
        "twitch",
        "twitter",
        "youtube",
        "bluesky",
    )

    template_name = "vgarchive/forms/organization-create.html"


class RunnerCreate(CreateView):
    model = Runner
    fields = (
        "name",
        "pronouns",
        "twitch",
        "youtube",
        "twitter",
        "bluesky",
    )

    template_name = "vgarchive/forms/runner-create.html"


class RunCreate(CreateView):
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
    template_name = "vgarchive/forms/run-create.html"
