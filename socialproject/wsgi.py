"""
WSGI config for socialproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

settings_module = "socialproject.settings" if "WEBSITE_HOSTNAME" in os.environ else "socialproject.settings"

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socialproject.settings')

application = get_wsgi_application()
