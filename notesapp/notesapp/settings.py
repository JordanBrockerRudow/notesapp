import os
from pathlib import Path
from configurations import Configuration
from configurations import values
import dj_database_url
import logging

from .secret import SECRET_KEY

from datetime import timedelta


class Dev(Configuration):
    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Admin Settings
    ADMINS = [("Notesapp Admin", "Admin@notesapp.com")]


    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = values.BooleanValue(True)

    ALLOWED_HOSTS = ['*']

    SECRET_KEY = SECRET_KEY


    # Application definition

    INSTALLED_APPS = [
        'rest_framework',
        'rest_framework.authtoken',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.sites',
        'django.contrib.staticfiles',
        'notes.apps.NotesConfig',
        'notesapp_auth.apps.NotesappAuthConfig',
        'crispy_forms',
        'crispy_bootstrap5',
        'debug_toolbar',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'allauth.socialaccount.providers.google',
        'drf_yasg',
        'django_filters',
        'versatileimagefield',
        'django_extensions'
    ]


    MIDDLEWARE = [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    # Debug's toolbar is only shown if IP Address is listed in Django's INTERNAL_IPS setting

    INTERNAL_IPS = [
        '127.0.0.1'
    ]

    ROOT_URLCONF = 'notesapp.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR/'templates',],
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

    # Bootstrap Crispy Forms

    CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
    CRISPY_TEMPLATE_PACK = 'bootstrap5'

    WSGI_APPLICATION = 'notesapp.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/3.2/ref/settings/#databases
    # How we would make use of different databases with django configurations
    DATABASES = values.DatabaseURLValue(f"sqlite:///{BASE_DIR}/db.sqlite3")
    # Admin settings
    # TO DO - Add Email
    ADMINS = [("Jordan", "jordan@email.com")]

    # Password Hashing
    # Argon2 Password Hashing Algorithm
    PASSWORD_HASHERS = [
        'django.contrib.auth.hashers.Argon2PasswordHasher',
        'django.contrib.auth.hashers.PBKDF2PasswordHasher',
        'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
        'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    ]


    # Password validation
    # https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

    # OAuth2 - Google login
    # SITE_ID tells the app which "Site" object to use these settings for
    SITE_ID = 1

    # Django Allauth creates a User object from a social account login
    # Since the Custom User model removed usernames, the
    # settings below will help ensure allauth doesn't fail
    ACCOUNT_USER_MODEL_USERNAME_FIELD = None
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_USERNAME_REQUIRED = False
    ACCOUNT_AUTHENTICATION_METHOD = "email"

    # Activation key valid for a week
    ACCOUNT_ACTIVATION_DAYS = 7


    # Internationalization
    # https://docs.djangoproject.com/en/3.2/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = values.Value("UTC")

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.2/howto/static-files/

    STATIC_URL = '/static/'
    # Media
    MEDIA_ROOT = BASE_DIR / "media"
    MEDIA_URL = "/media/"

    # Default primary key field type
    # https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
    # Authentication and Authorization
    # Point to Custom User Model
    AUTH_USER_MODEL= "notesapp_auth.User"

    # Django Registration Email
    # console email backend prints to terminal
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

    # Django Rest Framework

    # DRF
    # Note - DRF anonymous users are determined by IP address, so multiple clients at the same IP address would be considered the same "user".

    REST_FRAMEWORK = {
        "DEFAULT_AUTHENTICATION_CLASSES": [
            "rest_framework.authentication.BasicAuthentication",
            "rest_framework.authentication.SessionAuthentication",
            "rest_framework.authentication.TokenAuthentication",
            # SimpleJWT
            # https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html
            "rest_framework_simplejwt.authentication.JWTAuthentication",
        ],
        "DEFAULT_PERMISSION_CLASSES": [
          "rest_framework.permissions.IsAuthenticatedOrReadOnly"
        ],
        # Throttling
        # https://www.django-rest-framework.org/api-guide/throttling/
        "DEFAULT_THROTTLE_CLASSES": [
          "notes.api.throttling.AnonSustainedThrottle",
          "notes.api.throttling.AnonBurstThrottle",
          "notes.api.throttling.UserSustainedThrottle",
          "notes.api.throttling.UserBurstThrottle",
        ],
        "DEFAULT_THROTTLE_RATES": {
            "anon_sustained": "500/day",
            "anon_burst": "10/minute",
            "user_sustained": "5000/day",
            "user_burst": "100/minute",
        },
        # Pagination
        # https://www.django-rest-framework.org/api-guide/pagination/#limitoffsetpagination
        "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
        # Max per page
        "PAGE_SIZE": 100,
        # Django Filter
        # https://django-filter.readthedocs.io/
        "DEFAULT_FILTER_BACKENDS": [
            "django_filters.rest_framework.DjangoFilterBackend",
            "rest_framework.filters.OrderingFilter",
        ],
    }

    # Django Rest Framework Third-Party Libraries
    # https://django-rest-framework-simplejwt.readthedocs.io/en/latest/
    # https://django-versatileimagefield.readthedocs.io/en/latest/

    # JWT Refresh Token valid time - 7 days
    SIMPLE_JWT = {
        "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
        "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    }


    # SimpleJWT
    # https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html

    # Note - JWTs consist of three parts: header, payload and signature

    # 1. [Header]: consists of 'type' (usually jwt) and the algorithm ('alg') used to generate signature

    # 2. [Payload]: Can consist of any data (IE user_pk, token_type, exp)

    # 3. [Signature]: generated using a hash function as specified in the header.
    # Note - For a JWT, the input value to the HMAC256 is the base-64 encoded header, and the base-64 encoded payload, joined with a .. The secret that’s used is kept private.

    # To authenticate using JWT, the client sends the token in the 'Authorization' HTTP header, (usually with a 'Bearer' prefix)


    # JSON Web Tokens
    # https://jwt.io/introduction

    # JWT.IO
    # online tool to decode, verify and generate JWTs
    # https://jwt.io/

    # https://www.epochconverter.com/

    # Browsable API - Swagger OpenAPI Specification
    # https://swagger.io/specification/
    # https://github.com/axnsan12/drf-yasg
    SWAGGER_SETTINGS = {
        "SECURITY_DEFINITIONS": {
            "Token": {"type": "apiKey", "name": "Authorization", "in": "header"},
            "Basic": {"type": "basic"},
        }
    }

    # Logging Configuration Settings
    # This config sets up one handler with the ID console.
    # The handler will log to the console.

    LOGGING = {
            "version": 1,
            "disable_existing_loggers": False,
            "filters": {
                    "require_debug_false": {
                            # Error Emails are only sent in production enviroments
                            "()": "django.utils.log.RequireDebugFalse",
                    },
            },
            "formatters": {
                    "verbose": {
                            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
                            # Outputs the log level, time of the message (asctime), name of
                            # the module that generated the message, the process ID,
                            # thread ID, and lastly, the message.
                            "style": "{",
                    },
            },
            "handlers": {
                    "console": {
                            "class": "logging.StreamHandler",
                            "stream": "ext://sys.stdout",
                            "formatter": "verbose",
                    },
                    "mail_admins": {
                            "level": "ERROR",
                            "class": "django.utils.log.AdminEmailHandler",
                            "filters": ["require_debug_false"],
                    },
            },
            "loggers": {
                    # Django.request so that only unhandled exceptions get sent.
                    "django.request": {
                            "handlers": ["mail_admins"],
                            "level": "ERROR",
                            # Add propagate: True; so the stack traces are logged to the console during development.
                            "propagate": True,
                    },
            },
            "root": {
                    "handlers": ["console"],
                    "level": "DEBUG",
            },
    }

# Production
class Prod(Dev):
    DEBUG = False
    # Prevent secret keys committed in code, from being used in production
    SECRET_KEY = values.SecretValue()
