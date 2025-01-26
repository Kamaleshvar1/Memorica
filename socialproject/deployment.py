import os
from .settings import *
from .settings import BASE_DIR


SECRET_KEY = os.getenv('SECRET')
ALLOWED_HOSTS = [os.getenv('WEBSITE_HOSTNAME', '')]
CSRF_TRUSTED_ORIGINS = ['https://' + os.getenv('WEBSITE_HOSTNAME', 'https://memorica-bng4gdf5bygjajes.southindia-01.azurewebsites.net')]
DEBUG = False

# WhiteNoise configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')



conn_str = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
conn_str_params = {pair.split('=')[0]: pair.split('=')[1] for pair in conn_str.split(' ')}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'memorica',
        'USER': 'memorica',
        'PASSWORD': 'Shankam123*',
        'HOST': 'memorica.postgres.database.azure.com',
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require'
        }
    }
}

SOCIAL_AUTH_GOOGLE_CLIENT_ID = '202264358487-14p906v9pudrqo0gja1a58bgsa2k6fm2.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_SECRET = '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'