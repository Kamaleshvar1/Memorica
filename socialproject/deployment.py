import os
from .settings import *
from .settings import BASE_DIR


SECRET_KEY = os.getenv('SECRET')
ALLOWED_HOSTS = [os.getenv('WEBSITE_HOSTNAME', '')]
CSRF_TRUSTED_ORIGINS = ['https://' + os.getenv('WEBSITE_HOSTNAME', '')]
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
        'NAME': os.getenv('AZURE_DBNAME'),
        'USER': os.getenv('AZURE_DBUSER'),
        'PASSWORD': os.getenv('AZURE_DBPASSWORD'),
        'HOST': os.getenv('AZURE_DBHOST'),
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require'
        }
    }
}