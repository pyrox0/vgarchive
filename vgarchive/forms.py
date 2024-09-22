from django import forms
from vgarchive.runs import models as run_models


class RunnerIngestForm(forms.ModelForm):
    class Meta:
        model = run_models.Runner
        fields = (
            "name",
            "pronouns",
            "twitch",
            "youtube",
            "twitter",
            "bluesky",
        )
