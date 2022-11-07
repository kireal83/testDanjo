from django.apps import AppConfig

# 固定，不用动，app启动类


class App1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app1'
