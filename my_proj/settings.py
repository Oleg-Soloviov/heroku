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
#EMAIL_BACKEND = 'my_proj.mail_backends.MailgunEmailBackend'
#EMAIL_BACKEND = "my_proj.gmail_backends.GmailSmtpEmailBackend"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = "osoloviov2000@gmail.com"
EMAIL_HOST_PASSWORD = "Oleg152102"
EMAIL_USE_TLS = True


# SECURITY WARNING: don't run with debug turned on in production!
# set DEBUG virable on heroku to 'PRODUCTION'
MY_ENV = os.environ.get('DEBUG', 'False')

#~ if MY_ENV=='PRODUCTION':
    #~ DEBUG = False
ALLOWED_HOSTS = ["secret-mesa-26263.herokuapp.com"]
#~ else:
DEBUG = True
    #~ ALLOWED_HOSTS = ["127.0.0.1","10.0.2.2"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    'portfolio.apps.PortfolioConfig',
    'my_auth.apps.MyAuthConfig',
    'crispy_forms',
    'tinymce',
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

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


LOGIN_REDIRECT_URL = '/accounts/profile/'
LOGOUT_REDIRECT_URL = '/home/'

################ crispy forms ##########################
CRISPY_TEMPLATE_PACK = 'bootstrap3'

###################### TinyMCE ########################
TINYMCE_DEFAULT_CONFIG = {
    'height': '400px',
    'width': '100%',
    'background-color': 'maroon',
    'plugins': "table,paste,searchreplace,advhr,emotions,inlinepopups,style,preview,insertdatetime,",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
    'theme_advanced_buttons1_add' : "separator,insertdatetime,preview,separator,forecolor,backcolor",
    'theme_advanced_buttons2_add' : "hr,removeformat,visualaid,separator,sub,sup,separator,charmap,advhr,emotions,styleprops",
    'theme_advanced_buttons3' : "",
    
    'style_formats' : [
        {'title' : 'Bold text', 'inline' : 'b'},
        {'title' : 'Red text', 'inline' : 'span', 'styles' : {'color' : '#ff0000'}},
        {'title' : 'Red header', 'block' : 'h1', 'styles' : {'color' : '#ff0000'}},
        {'title' : 'Table row 1', 'selector' : 'tr', 'classes' : 'tablerow1'},
    ]

}

