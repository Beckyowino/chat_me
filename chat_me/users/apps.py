import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "chat_me.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import chat_me.users.signals  # noqa: F401
