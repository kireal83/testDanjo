"""
WSGI config for testDanjo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""
# 接收网络请求，默认放着，不要动！！！！

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testDanjo.settings')

application = get_wsgi_application()
