"""
Django settings for blagun_gordun_chuprin_stepanenko project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9e_v#^x_eh(@f&7w8@9u_5sl#rar(+km#7$s_cm1j1yqp5(d8j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SOME_VAR = 'Blagun'

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'didnotguess.apps.DidnotguessConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'blagun_gordun_chuprin_stepanenko.urls'

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
                'social_django.context_processors.backends',  # <--
                'social_django.context_processors.login_redirect',  # <--
            ],
        },
    },
]

WSGI_APPLICATION = 'blagun_gordun_chuprin_stepanenko.wsgi.application'

TEMPLATE_DIRS = ( 
    os.path.join(os.path.dirname(__file__),
    'templates').replace('\\','/'), 
)

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


AUTHENTICATION_BACKENDS = (
    # 'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'social.backends.github.GithubOAuth2',
    'social.backends.instagram.InstagramOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    # 'django.contrib.auth.backends.ModelBackend',
)
SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',  # <---
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)
#   google credentials
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '170292429057-8f6ji6s17qj2241ogsfc8mqar6n0f6df.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'rawglB_MX5seIHDKXS2GqDHq'

# Github #
SOCIAL_AUTH_GITHUB_KEY = '9fca0ad5a33911e8aa62'
SOCIAL_AUTH_GITHUB_SECRET = 'cfd573c7edf314fa3a475e5f150da0a6f371e4e2'
# SOCIAL_AUTH_GITHUB_SCOPE = ['user:email']
GITHUB_REQUIRE_VERIFIED_EMAIL = True

SOCIAL_AUTH_FACEBOOK_KEY = '118415938743411'
SOCIAL_AUTH_FACEBOOK_SECRET = '4add1feef01df4e876e962ed2f31130e'

SOCIAL_AUTH_INSTAGRAM_KEY = 'e95aad2dea4c414586b23929ef75c656'
SOCIAL_AUTH_INSTAGRAM_SECRET = '13e622f595fa423598c8ac085cf5417b'

LOGIN_URL = '/didnotguess/login'
LOGOUT_URL = '/didnotguess/logout'
LOGIN_REDIRECT_URL = '/didnotguess/'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

