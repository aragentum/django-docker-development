from .base import *


DEBUG = True

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_web',
        'USER': 'django_web',
        'PASSWORD': 'django_web',
        'HOST': 'dev-db',
        'PORT': 5432
    },
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'console_formatter': {
            'format': '[%(asctime)s]:[%(process)d] | [%(levelname)s] | %(name)-15s - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console_formatter'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO'
        },
        'web': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False
        }
    }
}
