import os


PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Herman Caldara', 'hermancaldara@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT_PATH, 'blog.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'America/Sao_Paulo'

LANGUAGE_CODE = 'pt-br'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = os.path.join(PROJECT_ROOT_PATH, 'site_media')

MEDIA_URL = '/site_media'

ADMIN_MEDIA_PREFIX = '/admin_media/'

SECRET_KEY = '$^8gqj2*voz1gbpmm7#25087@7&h9de1!vrh!7oz260#t+g$hn'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    "django.template.loaders.filesystem.load_template_source",
    "django.template.loaders.app_directories.load_template_source",
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT_PATH, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.syndication',
    'django.contrib.markup',
    'apps.posts',
    'apps.contato',
    'pagination',
    'taggit',
)

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'hermancaldara@gmail.com'
EMAIL_HOST_PASSWORD = '123456'
EMAIL_SUBJECT_PREFIX = '[RiceTeam]'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
