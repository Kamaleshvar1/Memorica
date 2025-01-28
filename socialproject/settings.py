from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY SETTINGS
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-bs^g4lm8bf&=+d^qb4$x3-(r3$6-v)h-k&8pc&tva@cc9usg2@')
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# SITE SETTINGS
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')
CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED_ORIGINS', 'http://localhost').split(',')

ROOT_URLCONF = 'socialproject.urls'
WSGI_APPLICATION = 'socialproject.wsgi.application'

# APPLICATION DEFINITION
INSTALLED_APPS = [
    'django.contrib.admin',
    'users',
    'posts',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

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

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'users/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# DATABASE SETTINGS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'memorica'),
        'USER': os.getenv('DB_USER', 'memorica'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST', 'memorica.postgres.database.azure.com'),
        'PORT': os.getenv('DB_PORT', '5432'),
        'OPTIONS': {
            'sslmode': 'require'
        }
    }
}

# AUTHENTICATION SETTINGS
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# SOCIAL AUTH SETTINGS
SITE_ID = 3
ACCOUNT_EMAIL_VERIFICATION = 'none'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online', 'prompt': 'select_account'},
        'OAUTH_PKCE_ENABLED': True,
        'SITE': {
            'id': SITE_ID,
        }
    }
}

SOCIAL_AUTH_GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
SOCIAL_AUTH_GOOGLE_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')

# SESSION SETTINGS
SESSION_COOKIE_AGE = 86400
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# INTERNATIONALIZATION
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# STATIC FILES SETTINGS
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# MEDIA FILES SETTINGS
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# EMAIL SETTINGS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# AZURE STORAGE SETTINGS
AZURE_ACCOUNT_NAME = os.getenv('AZURE_ACCOUNT_NAME', 'memoricastorage')
AZURE_ACCOUNT_KEY = os.getenv('AZURE_ACCOUNT_KEY')
AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'
AZURE_STATIC_CONTAINER = 'static'
AZURE_MEDIA_CONTAINER = 'media'
AZURE_SSL = True

# STORAGE BACKEND SETTINGS
DEFAULT_FILE_STORAGE = 'socialproject.storage_backends.AzureMediaStorage'
STATICFILES_STORAGE = 'socialproject.storage_backends.AzureStaticStorage'

# URLs
MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{AZURE_MEDIA_CONTAINER}/'
STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{AZURE_STATIC_CONTAINER}/'
LOGIN_URL = 'login'
LOGOUT_REDIRECT_URL = 'logout'
LOGIN_REDIRECT_URL = 'feed'

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

# MISC SETTINGS
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'