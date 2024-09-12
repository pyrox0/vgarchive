import locale

from django.views.generic.detail import DetailView
from django.utils.html import format_html
from django.urls import reverse

import django_tables2 as tables

from .models import Organization
from vgarchive.charities.models import Charity
from vgarchive.views import VGArchiveMetaTable


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
        return context


class OrganizationTable(tables.Table):
    class Meta(VGArchiveMetaTable):
        model = Organization
        order_by = "-name"
        sequence = (
            "name",
            "active",
            "total_raised",
            "twitch",
            "twitter",
            "youtube",
        )
        exclude = (
            "banner",
            "description",
            "homepage",
            "icon",
            "id",
        )

    name = tables.Column(verbose_name="Organization Name")
    total_raised = tables.Column(verbose_name="Donation Total", localize=True)
    twitch = tables.Column(verbose_name="Twitch", orderable=False)
    twitter = tables.Column(verbose_name="Twitter", orderable=False)
    youtube = tables.Column(verbose_name="Youtube", orderable=False)

    def render_homepage(self, value):  # noqa
        return format_html(
            f'<a class="external-link link-info" href="{value}">Homepage</a>'
        )

    def render_name(self, value, record):  # noqa
        return format_html(
            f'<a class="text-2xl font-bold link link-primary" href="{reverse("organization-detail", args=[record.id])}">{value}</a>'
        )

    def render_total_raised(self, value):  # noqa
        return format_html(
            f'<p class="text-success font-bold">{locale.currency(value, True, True, False)}</p>'
        )

    def render_twitch(self, value, record):  # noqa
        return format_html(
            f'<a class="link text-primary" aria-label="{record.name} Twitch Channel" href="https://twitch.tv/{value}"><i class="bi-twitch text-3xl"></i></a>'
        )

    def render_twitter(self, value, record):  # noqa
        return format_html(
            f'<a class="link text-info" aria-label="{record.name} Twitter Page" href="https://x.com/{value}"><i class="bi-twitter text-3xl"></i></a>'
        )

    def render_youtube(self, value, record):  # noqa
        return format_html(
            f'<a class="link text-error" aria-label="{record.name} Youtube Channel" href="https://youtube.com/{value}"><i class="bi-youtube text-3xl"></i></a>'
        )


class OrganizationListView(tables.SingleTableView):
    model = Organization
    table_class = OrganizationTable
    template_name = "organization-list.html"
