from django.apps import AppConfig

from apps.utils.print_colors import _blue


class MainConfig(AppConfig):
    name = 'apps.main'
    verbose_name = 'main'

    def ready(self):
        print(_blue('Ready Main'))
