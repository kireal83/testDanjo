"""
ASGI config for testDanjo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""
# 接收网络请求，默认放着，不要动！！！！danjo3异步
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testDanjo.settings')

application = get_asgi_application()
