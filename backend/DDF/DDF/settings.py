"""
Django settings for DDF project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PARENT_DIR = Path(__file__).resolve().parent.parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$i=)al8qof7e8t6@f*!=(-l4#ca(u*1a3ax5y!=f+sa5)ex!9n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'authentication',
    'user',
    'faculty',
    'committee',
    'hod',
    'request',
    'transaction',
    'django.test'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DDF.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PARENT_DIR,'frontend','build')],
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

WSGI_APPLICATION = 'DDF.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
	    'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ddf_swe', 
        'USER': 'sammy', 
        'PASSWORD': 'pa$$word',
        'HOST': '127.0.0.1', 
        'PORT': '5432',
    },
    'test': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test_ddf_swe', 
        'USER': 'sammy', 
        'PASSWORD': 'pa$$word',
        'HOST': '127.0.0.1', 
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

STATIC_URL = 'static/'

STATICFILES_DIRS=[
    os.path.join(PARENT_DIR,'frontend','build','static')
]

STATIC_ROOT = os.path.join(BASE_DIR,'static')

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES' : [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES' : [
        'rest_framework.authentication.SessionAuthentication',
    ],
}

CORS_ORIGIN_ALLOW_ALL=True

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'authentication.CustomUser'

AUTHENTICATION_BACKENDS = ['authentication.backends.FacultyUserBackend', 'authentication.backends.CommitteeUserBackend', 'authentication.backends.HodUserBackend', 'django.contrib.auth.backends.ModelBackend', ]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'ddf.cse.iith@gmail.com'  
EMAIL_HOST_PASSWORD = 'czfdefueigazdoyp'  

TEST_RUNNER = 'django.test.runner.DiscoverRunner'