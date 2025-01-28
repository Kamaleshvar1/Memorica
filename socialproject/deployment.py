import os
from .settings import *
from .settings import BASE_DIR

# Override settings for production
DEBUG = False

# Security settings
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
ALLOWED_HOSTS = ['memorica.social', 'memorica-bng4gdf5bygjajes.southindia-01.azurewebsites.net']
CSRF_TRUSTED_ORIGINS = ['https://memorica.social', 'https://memorica-bng4gdf5bygjajes.southindia-01.azurewebsites.net']

# Static files configuration
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'socialproject.storage_backends.AzureStaticStorage'

# Database configuration
if os.getenv('AZURE_POSTGRESQL_CONNECTIONSTRING'):
    conn_str = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
    conn_str_params = {pair.split('=')[0]: pair.split('=')[1] for pair in conn_str.split(' ')}

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': conn_str_params.get('dbname', os.getenv('DB_NAME')),
            'USER': conn_str_params.get('user', os.getenv('DB_USER')),
            'PASSWORD': conn_str_params.get('password', os.getenv('DB_PASSWORD')),
            'HOST': conn_str_params.get('host', os.getenv('DB_HOST')),
            'PORT': conn_str_params.get('port', os.getenv('DB_PORT')),
            'OPTIONS': {
                'sslmode': 'require'
            }
        }
    }

# Azure Storage settings
AZURE_ACCOUNT_NAME = os.getenv('AZURE_ACCOUNT_NAME')
AZURE_ACCOUNT_KEY = os.getenv('AZURE_ACCOUNT_KEY')
AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'

# Storage backends
DEFAULT_FILE_STORAGE = 'socialproject.storage_backends.AzureMediaStorage'
STATICFILES_STORAGE = 'socialproject.storage_backends.AzureStaticStorage'

# URLs
MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{AZURE_MEDIA_CONTAINER}/'
STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{AZURE_STATIC_CONTAINER}/'