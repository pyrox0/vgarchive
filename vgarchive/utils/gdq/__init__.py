"""
Module for extracting data from the Games Done Quick Donation Tracker API.

The tracker API is currently undocumented, so this is a manual implementation for now.
There may be an opportunity for doing more
"""

import requests

# These tags should result in that run being removed
# since these signify non-run interstitial content.
# This isn't perfect, and there's probably some that we miss.
# These filters will be refined as we try to do more regular imports.

# tags/priority_tags
GDQ_EXCLUDE_TAGS = [
    "preshow",
    "opener",
    "checkpoint",
    "tas",
    # Special FF Interstitials
    "chomp",
]
# twitch_name
GDQ_EXCLUDE_TWITCH_NAMES = [
    "Special Events",
    "Just Chatting",
]
# display_name
GDQ_EXCLUDE_DISPLAY_NAMES = [
    "Sleep",
    "Finale",
]
