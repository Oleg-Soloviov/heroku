"""
Django settings for my_proj project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import dj_database_url

from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w-i9r*+qj$!hfom7$f#qcqmnfq5v+e*&@nx5(v(2k4mi)-3f3b'


ADMINS = [('Oleg', 'osoloviov@mail.ru'), ('Oleg', 'osoloviov2000@gmail.com')]
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# SECURITY WARNING: don't run with debug turned on in production!
# set DEBUG virable on heroku to 'PRODUCTION'
MY_ENV = os.environ.get('DEBUG', 'False')

if MY_ENV=='PRODUCTION':
    DEBUG = False
    ALLOWED_HOSTS = ["secret-mesa-26263.herokuapp.com"]
else:
    DEBUG = True
    ALLOWED_HOSTS = ["127.0.0.1","secret-mesa-26263.herokuapp.com"]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'portfolio',
    'crispy_forms',
    'tinymce',
#    'django_wysiwyg',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',    # FOR I18N: after session, before common
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'my_proj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'my_proj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
  ('en', _('English')),
  ('ru', _('Russian')),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

################ crispy forms ##########################
CRISPY_TEMPLATE_PACK = 'bootstrap3'

###################### TinyMCE ########################
TINYMCE_JS_URL = os.path.join(STATIC_URL+'tiny_mce/tiny_mce_src.js')
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace,advhr,emotions,inlinepopups,style,preview,insertdate,inserttime,zoom,formats",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
    'theme_advanced_buttons1_add' : "separator,insertdate,inserttime,preview,zoom,separator,forecolor,backcolor",
    'theme_advanced_buttons2_add' : "hr,removeformat,visualaid,separator,sub,sup,separator,charmap,advhr,emotions,styleprops",
    'theme_advanced_buttons3' : "",
    
    'style_formats' : [
        {'title' : 'Bold text', 'inline' : 'b'},
        {'title' : 'Red text', 'inline' : 'span', 'styles' : {'color' : '#ff0000'}},
        {'title' : 'Red header', 'block' : 'h1', 'styles' : {'color' : '#ff0000'}},
        {'title' : 'Table row 1', 'selector' : 'tr', 'classes' : 'tablerow1'}
    ]

}

TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True

