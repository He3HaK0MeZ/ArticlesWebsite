from django.apps import AppConfig


class Myapp1Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "modules.blog"
    verbose_name = "Приложение1"
