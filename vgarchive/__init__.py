from django_icons.renderers.icon import IconRenderer


class BootstrapIconRenderer(IconRenderer):
    """Render a Bootstrap 3 icon."""

    def get_class(self):  # noqa
        return f"bi-{self.name}"

    def get_attrs(self):  # noqa
        attrs = super().get_attrs()
        aria_label = self.kwargs.get("aria_label")
        if aria_label:
            attrs["aria-label"] = aria_label
        tabindex = self.kwargs.get("tabindex")
        if tabindex:
            attrs["tabindex"] = tabindex

        return attrs
