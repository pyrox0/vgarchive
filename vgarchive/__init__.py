from django_icons.renderers.icon import IconRenderer


class BootstrapIconRenderer(IconRenderer):
    """Render a Bootstrap 3 icon."""

    def get_class(self):  # noqa
        return f"bi-{self.name}"
