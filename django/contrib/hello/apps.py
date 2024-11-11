from django.apps import AppConfig


class HelloConfig(AppConfig):
    name = 'django.contrib.hello'
    verbose_name = 'Hello World'
    default_auto_field = 'django.db.models.AutoField'
