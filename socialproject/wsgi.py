import os

from django.core.wsgi import get_wsgi_application

# Use deployment settings if WEBSITE_HOSTNAME exists (production environment)
# Otherwise use default settings
settings_module = "socialproject.deployment" if "WEBSITE_HOSTNAME" in os.environ else "socialproject.settings"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()