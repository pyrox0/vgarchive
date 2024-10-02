from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import requests

__all__ = ["validate_bluesky"]


def validate_bluesky(value: str) -> None | ValidationError:
    url = "https://public.api.bsky.app/xrpc/app.bsky.actor.getProfile"
    headers = {
        "Accept": "application/json",
    }
    params = {
        "actor": value,
    }
    response = requests.get(url, params=params, headers=headers, timeout=2)

    if response.status_code == 400:
        raise ValidationError(
            _("%(value)s is not a valid Bluesky account."),
            params={"value": value},
        )
    if response.status_code == 401:
        raise ValidationError(_("Failed to fetch Bluesky data, try again later."))
