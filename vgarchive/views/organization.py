import locale

from django.db.models.aggregates import Sum
from django.views.generic.detail import DetailView
from django.utils.html import format_html

import django_tables2 as tables
import django_filters as filters
import django_filters.views as filter_views

from vgarchive.models.organization import Organization
from vgarchive.models.charity import Charity
from vgarchive.views import VGArchiveMetaTable, VGArchiveForm
from vgarchive import utils

__all__ = [
    "OrganizationDetailView",
    "OrganizationListView",
]


class OrganizationDetailView(DetailView):
    model = Organization
    template_name = "vgarchive/detail/organization.html"

    def get_context_data(self, **kwargs) -> dict:  # noqa
        # Get context
        context = super().get_context_data(**kwargs)
        context["events"] = self.object.event_set.all()
        context["charities"] = Charity.objects.filter(  # type:ignore
            id__in=context["events"].values_list("charity", flat=True)
        )
        context["title"] = self.object.name + " | VGArchive"
        return context


class OrganizationTable(tables.Table):
    class Meta(VGArchiveMetaTable):
        model = Organization
        order_by = "-name"
        sequence = (
            "name",
            "donation_total",
            "tracker",
            "twitch",
            "twitter",
            "youtube",
            "bluesky",
        )
        exclude = (
            "banner",
            "description",
            "homepage",
            "icon",
            "id",
        )

    name = tables.Column(
        verbose_name="Organization Name",
        linkify=True,
        attrs={"a": {"class": "text-2xl font-bold link link-primary"}},
    )
    donation_total = tables.Column(verbose_name="Donation Total", localize=True)
    tracker = tables.URLColumn(
        text=format_html('<i class="bi-archive text-3xl"></i>'),
        attrs={
            "a": {
                "class": "link text-info",
                "aria-label": lambda record: f"{record.name} Donation Tracker",
            }
        },
        orderable=False,
    )
    twitch = utils.views.TwitchColumn(verbose_name="Twitch", orderable=False)
    twitter = utils.views.TwitterColumn(verbose_name="Twitter", orderable=False)
    youtube = utils.views.YoutubeColumn(verbose_name="Youtube", orderable=False)
    bluesky = utils.views.BlueskyColumn(verbose_name="Bluesky", orderable=False)

    def render_donation_total(self, value):  # noqa
        return format_html(
            f'<p class="text-success font-bold">{locale.currency(value, True, True, False)}</p>'
        )

    def order_donation_total(self, queryset, is_descending):  # noqa
        queryset = queryset.annotate(
            donation_total=Sum("event__donation_total")
        ).order_by(("-" if is_descending else "") + "donation_total")
        return (queryset, True)


class OrganizationFilter(filters.FilterSet):
    class Meta:
        model = Organization
        form = VGArchiveForm
        fields = ("name", "donation_total")
        exclude = ("homepage", "youtube", "twitter", "twitch")

    donation_total = filters.NumberFilter(label="Donation Total:")


class OrganizationListView(tables.SingleTableMixin, filter_views.FilterView):  # type:ignore
    model = Organization
    table_class = OrganizationTable
    template_name = "vgarchive/list/organization.html"

    filterset_class = OrganizationFilter
