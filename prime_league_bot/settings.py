"""
Django settings for prime_league_bot project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import errno
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env()
environ.Env.read_env()  # reading .env file

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('DJANGO_SECRET_KEY', default="")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', default=False)
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", cast=str, default=[])

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd party
    'django_extensions',
    # own
    'app_prime_league',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'prime_league_bot.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 ]
        ,
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

WSGI_APPLICATION = 'prime_league_bot.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env.str('DB_NAME'),
        'USER': env.str('DB_USER'),
        'PASSWORD': env.str('DB_PASSWORD'),
        'HOST': env.str('DB_HOST'),
        'PORT': env.str('DB_PORT'),
        'CONN_MAX_AGE': 3600,
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'de-de'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

LEAGUES_URI = "https://www.primeleague.gg/de/leagues/"
AJAX_URI = "https://www.primeleague.gg/ajax/"

MATCH_URI = "https://www.primeleague.gg/de/leagues/matches/"
TEAM_URI = "https://www.primeleague.gg/de/leagues/teams/"

DEFAULT_TELEGRAM_CHAT_ID = env.str("TG_CHAT_ID", None)

STORAGE_DIR = os.path.join(BASE_DIR, "storage", )

TELEGRAM_BOT_KEY = env.str("TELEGRAM_BOT_API_KEY")
TG_DEVELOPER_GROUP = env.int("TG_DEVELOPER_GROUP")
TELEGRAM_LIVETICKER_KEY = env.str("TELEGRAM_LIVETICKER_API_KEY")

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

DISCORD_BOT_KEY = env.str("DISCORD_API_KEY")
DISCORD_APP_CLIENT_ID = env.int("DISCORD_APP_CLIENT_ID")
DISCORD_DEFAULT_GUILD = "***REMOVED***"

LOGIN_URL = "/admin/login/"

LOGGING_DIR = os.path.join(BASE_DIR, "logs", )
try:
    os.mkdir(LOGGING_DIR)
except OSError as exc:
    if exc.errno != errno.EEXIST:
        raise exc
    pass

if not DEBUG:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'to_file': {
                'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
                'datefmt': "%d/%b/%Y %H:%M:%S"
            },
            'to_console': {
                'format': '[%(levelname)s] %(name)s: %(message)s'
            },
        },
        'handlers': {
            'console': {
                'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
                'formatter': 'to_console',
                'class': 'logging.StreamHandler',
            },
            'django_file': {
                'level': os.getenv('DJANGO_LOG_LEVEL', 'WARNING'),
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': os.path.join(LOGGING_DIR, 'django.log'),
                'when': 'midnight',
                'formatter': 'to_file',
            },
            'periodic_handler': {
                'level': 'INFO',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': os.path.join(LOGGING_DIR, 'periodic.log'),
                'when': 'midnight',
                'formatter': 'to_file',
            },
            'periodic_verbose_handler': {
                'level': 'DEBUG',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': os.path.join(LOGGING_DIR, 'periodic_verbose.log'),
                'when': 'midnight',
                'formatter': 'to_file',
            },
            'main_handler': {
                'level': 'INFO',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': os.path.join(LOGGING_DIR, 'main.log'),
                'when': 'midnight',
                'formatter': 'to_file',
            },
            'main_verbose_handler': {
                'level': 'DEBUG',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': os.path.join(LOGGING_DIR, 'main_verbose.log'),
                'when': 'midnight',
                'formatter': 'to_file',
            },
            'notifications_handler': {
                'level': 'DEBUG',
                'class': 'logging.handlers.WatchedFileHandler',
                'filename': os.path.join(LOGGING_DIR, 'notifications.log'),
                'formatter': 'to_file',
            },
            'commands_handler': {
                'level': 'DEBUG',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': os.path.join(LOGGING_DIR, 'commands.log'),
                'when': 'midnight',
                'formatter': 'to_file',
            }
        },
        'loggers': {
            'django': {
                'handlers': ['console', 'django_file'],
                'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
                'propagate': False,
            },
            'main_logger': {
                'handlers': ['main_handler', 'main_verbose_handler'],
                'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
                'propagate': False,
            },
            'periodic_logger': {
                'handlers': ['periodic_handler', 'periodic_verbose_handler'],
                'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
                'propagate': False,
            },
            'notifications_logger': {
                'handlers': ['notifications_handler'],
                'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
                'propagate': False,
            },
            'commands_logger': {
                'handlers': ['commands_handler', ],
                'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
                'propagate': False,
            }
        }
    }
