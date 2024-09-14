import locale

from django.views.generic.detail import DetailView
from django.utils.html import format_html
from django.urls import reverse

import django_tables2 as tables
import django_filters as filters
import django_filters.views as filter_views

from .models import Organization
from vgarchive.charities.models import Charity
from vgarchive.views import VGArchiveMetaTable, VGArchiveForm
from vgarchive import utils


class OrganizationDetailView(DetailView):
    model = Organization
    template_name = "organization-detail.html"

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
            "active",
            "donation_total",
            "tracker",
            "twitch",
            "twitter",
            "youtube",
            "bluesky",
            "facebook",
        )
        exclude = (
            "banner",
            "description",
            "homepage",
            "icon",
            "id",
        )

    name = tables.Column(verbose_name="Organization Name")
    donation_total = tables.Column(verbose_name="Donation Total", localize=True)
    tracker = tables.Column(orderable=False)
    twitch = tables.Column(verbose_name="Twitch", orderable=False)
    twitter = tables.Column(verbose_name="Twitter", orderable=False)
    youtube = tables.Column(verbose_name="Youtube", orderable=False)
    bluesky = tables.Column(verbose_name="Bluesky", orderable=False)
    facebook = tables.Column(verbose_name="Facebook", orderable=False)

    def render_homepage(self, value):  # noqa
        return utils.render_homepage(value)

    def render_name(self, value, record):  # noqa
        return format_html(
            f'<a class="text-2xl font-bold link link-primary" href="{reverse("organization-detail", args=[record.id])}">{value}</a>'
        )

    def render_donation_total(self, value):  # noqa
        return format_html(
            f'<p class="text-success font-bold">{locale.currency(value, True, True, False)}</p>'
        )

    def render_twitch(self, value, record):  # noqa
        return utils.render_twitch(record.name, value)

    def render_twitter(self, value, record):  # noqa
        return utils.render_twitter(record.name, value)

    def render_youtube(self, value, record):  # noqa
        return utils.render_youtube(record.name, value)

    def render_bluesky(self, value, record):  # noqa
        return utils.render_bluesky(record.name, value)


BOOLEAN_CHOICES = (
    (True, "Yes"),
    (False, "No"),
)


class OrganizationFilter(filters.FilterSet):
    class Meta:
        model = Organization
        form = VGArchiveForm
        fields = ("name", "active", "donation_total")
        exclude = ("homepage", "youtube", "twitter", "twitch")

    donation_total = filters.NumberFilter(label="Donation Total:")
    active = filters.ChoiceFilter(label="Active?:", choices=BOOLEAN_CHOICES)


class OrganizationListView(tables.SingleTableMixin, filter_views.FilterView):  # type:ignore
    model = Organization
    table_class = OrganizationTable
    template_name = "organization-list.html"

    filterset_class = OrganizationFilter
