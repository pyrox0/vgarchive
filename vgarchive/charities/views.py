import locale

from django.views.generic.detail import DetailView
from django.utils.html import format_html
from django.urls import reverse

import django_tables2 as tables
import django_filters as filters
import django_filters.views as filter_views

from .models import Charity
from vgarchive.views import VGArchiveMetaTable, VGArchiveForm
from vgarchive import utils


class CharityDetailView(DetailView):
    model = Charity
    template_name = "charity-detail.html"

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
        exclude = ("id", "short_name", "icon")
        sequence = (
            "name",
            "homepage",
            "donation_total",
            "founded",
        )

    name = tables.Column(verbose_name="Name")
    homepage = tables.Column(verbose_name="Homepage", orderable=False)
    donation_total = tables.Column(verbose_name="Donation Total", localize=True)
    founded = tables.Column(verbose_name="Year Founded", localize=False)
    twitter = tables.Column(verbose_name="Twitter", localize=False, orderable=False)
    youtube = tables.Column(verbose_name="Youtube", localize=False, orderable=False)
    linkedin = tables.Column(verbose_name="Linkedin", localize=False, orderable=False)
    bluesky = tables.Column(verbose_name="Bluesky", localize=False, orderable=False)
    facebook = tables.Column(verbose_name="Facebook", localize=False, orderable=False)

    def render_homepage(self, value):  # noqa
        return format_html(
            f'<a class="external-link link-info" href="{value}">Homepage</a>'
        )

    def render_name(self, value, record):  # noqa
        return format_html(
            f'<a class="text-2xl font-bold link link-primary" href="{reverse("charity-detail", args=[record.id])}">{value}</a>'
        )

    def render_donation_total(self, value):  # noqa
        return format_html(
            f'<p class="text-success font-bold">{locale.currency(value, True, True, False)}</p>'
        )

    def render_twitter(self, value, record):  # noqa
        return utils.render_twitter(record.name, value)

    def render_youtube(self, value, record):  # noqa
        return utils.render_youtube(record.name, value)

    def render_bluesky(self, value, record):  # noqa
        return utils.render_bluesky(record.name, value)

    def render_facebook(self, value, record):  # noqa
        return utils.render_facebook(record.name, value)

    def render_linkedin(self, value, record):  # noqa
        return utils.render_linkedin(record.name, value)


class CharityFilter(filters.FilterSet):
    class Meta:
        model = Charity
        form = VGArchiveForm
        fields = ("name", "founded")
        exclude = "icon"

    name = filters.CharFilter(label="Name:", lookup_expr="icontains")
    founded = filters.NumberFilter(label="Founded After:", lookup_expr="gt")


class CharityListView(tables.SingleTableMixin, filter_views.FilterView):  # type:ignore
    model = Charity
    table_class = CharityTable
    template_name = "charity-list.html"

    filterset_class = CharityFilter
