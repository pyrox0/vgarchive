from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from vgarchive.models.organization import Organization
from vgarchive.models import DataSources


def _validate_tracker_type(value: DataSources) -> None | ValidationError:
    if value == DataSources.MANUAL:
        raise ValidationError(
            _(
                'Using the "Manual Import" tracker type with this form is not allowed. Use the "Data Creation" form instead.'
            )
        )


class OrganizationImportForm(forms.Form):
    organization = forms.ModelChoiceField(
        queryset=Organization.objects.all(),  # type:ignore
        required=True,
        label="Organization",
        help_text="All events from tracker URL listed will be added to this organization.",
    )
    tracker_url = forms.URLField(
        required=True,
        label="Tracker URL",
        help_text="Tracker to import events from",
    )
    tracker_type = forms.ChoiceField(
        choices=DataSources,
        initial=DataSources.TRACKER,
        required=True,
        label="Tracker Type",
        help_text="The type of the tracker.",
        validators=[_validate_tracker_type],
    )
