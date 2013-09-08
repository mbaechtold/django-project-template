# -*- coding: utf-8 -*-
import os
from configurations import values


class DevMixin(object):
    DEBUG = True
    TEMPLATE_DEBUG = True

    @property
    def DATABASES(self):
        SQLITE_ROOT = os.path.join(super(DevMixin, self).PROJECT_ROOT, 'database')
        try:
            os.makedirs(SQLITE_ROOT)
        except OSError:
            pass

        return {
            'default': {
                # Choose 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle' from 'django.db.backends'.
                'ENGINE': 'django.db.backends.sqlite3',
                # Name of database or path to database file if using sqlite3.
                'NAME': os.path.join(SQLITE_ROOT, 'dev.sqlite3'),
                # The following settings are not used with sqlite3:
                'USER': '',
                'PASSWORD': '',
                # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
                'HOST': '',
                # Set to empty string for default.
                'PORT': '',
            }
        }

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


class ProdMixin(object):
    DEBUG = False
    TEMPLATE_DEBUG = False

    # MAYBE: Instead of using many ``SecretValue()`` use only one ``DictValue()``. To be revised when deploying.
    DATABASES = {
        'default': {
            # Choose 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle' from 'django.db.backends'.
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            # Name of database or path to database file if using sqlite3.
            'NAME': values.SecretValue(environ_name='DJANGO_DATABASE_DEFAULT_NAME'),
            # The following settings are not used with sqlite3:
            'USER': values.SecretValue(environ_name='DJANGO_DATABASE_DEFAULT_USER'),
            'PASSWORD': values.SecretValue(environ_name='DJANGO_DATABASE_DEFAULT_PASSWORD'),
            # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
            'HOST': '',
            # Set to empty string for default.
            'PORT': '',
        }
    }

    # Hosts/domain names that are valid for this site; required if DEBUG is False
    # See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = values.ListValue([])


class MobileSiteMixin(object):
    SITE_ID = 2

    @property
    def TEMPLATE_DIRS(self):
        return (
            os.path.normpath(os.path.join(super(MobileSiteMixin, self).WEBSITE_ROOT, 'templates', 'sites', 'mobile')),
        ) + super(MobileSiteMixin, self).TEMPLATE_DIRS