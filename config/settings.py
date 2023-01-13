import os
from pathlib import Path
from django.core.management.utils import get_random_secret_key


BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG=False
# DEBUG=True

ALLOWED_HOSTS=['*']

CSRF_TRUSTED_ORIGINS=CORS_ORIGIN_WHITELIST=['https://012retwitchapi.aheahe1919.repl.co']

# シークレットキーを都度作成する
SECRET_KEY=get_random_secret_key()

# ajaxへpostする際のサイズ上限を指定
DATA_UPLOAD_MAX_MEMORY_SIZE = None

# The number of GET/POST parameters exceeded settings.DATA_UPLOAD_MAX_NUMBER_FIELDS.
DATA_UPLOAD_MAX_NUMBER_FIELDS = None

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'applications.apps.ApplicationsConfig',
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES={
	'default':{
		'ENGINE':'django_cockroachdb',
		'NAME':os.environ['NAME'],
		'USER':os.environ['USER'],
		'PASSWORD':os.environ['PASSWORD'],
		'HOST':os.environ['HOST'],
		'PORT':os.environ['PORT'],
		'OPTIONS': {
			'sslmode':'verify-full',
		},
	},
}

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

LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# https://devcenter.heroku.com/ja/articles/django-assets
# Heroku推奨の方法
STATIC_URL = '/static/'
STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# この処理を追加することで settings.py の DEBUG が False でも local_settings があればデバッグ環境だと判断されて runserver が可能になる→DEBUGを切り替える必要もなくなる
try:
	from .local_settings import *
except ImportError:
	pass

# Authentication
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'