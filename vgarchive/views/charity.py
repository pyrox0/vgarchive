import locale

from django.db.models.aggregates import Sum
from django.views.generic.detail import DetailView
from django.utils.html import format_html

import django_tables2 as tables
import django_filters as filters
import django_filters.views as filter_views

from vgarchive.models.charity import Charity
from vgarchive.views import VGArchiveMetaTable, VGArchiveForm
from vgarchive import utils

__all__ = [
    "CharityDetailView",
    "CharityListView",
]


class CharityDetailView(DetailView):
    model = Charity
    template_name = "vgarchive/detail/charity.html"

    def get_context_data(self, **kwargs) -> dict:  # noqa
        # Get context
        context = super().get_context_data(**kwargs)
        context["events"] = self.object.event_set.all()
        context["title"] = self.object.name + " | VGArchive"
        context["description"] = (
            f"Details page for the {self.object.name} charity on VGArchive, the open charity video game marathon search engine."
        )

        return context


class CharityTable(tables.Table):
    class Meta(VGArchiveMetaTable):
        model = Charity
        order_by = "-name"
        exclude = (
            "id",
            "short_name",
            "icon",
            "founded",
        )
        sequence = (
            "name",
            "homepage",
            "donation_total",
            "bluesky",
            "twitter",
            "youtube",
        )

    name = tables.Column(
        linkify=True,
        verbose_name="Name",
        attrs={"a": {"class": "text-2xl font-bold link link-primary"}},
    )
    homepage = utils.views.HomepageColumn(verbose_name="Homepage", orderable=False)
    donation_total = tables.Column(verbose_name="Donation Total", localize=True)
    founded = tables.Column(verbose_name="Year Founded", localize=False)
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


class CharityFilter(filters.FilterSet):
    class Meta:
        model = Charity
        form = VGArchiveForm
        fields = ["name"]  # noqa
        exclude = ("icon", "founded")

    name = filters.CharFilter(label="Name:", lookup_expr="icontains")


class CharityListView(tables.SingleTableMixin, filter_views.FilterView):  # type:ignore
    model = Charity
    table_class = CharityTable
    template_name = "vgarchive/list/charity.html"

    filterset_class = CharityFilter
