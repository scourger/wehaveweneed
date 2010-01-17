# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = '))-(d#^$+r7i9&v)rgu6=7y25wpkt8n9+uy^w6z7zpc)#=!7l^'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'wehaveweneed.urls'

AUTH_PROFILE_MODULE = 'web.userprofile'

LOGIN_URL = '/login'
LOGOUT_URL = '/logout'
LOGIN_REDIRECT_URL = '/'

HAYSTACK_SITECONF = 'wehaveweneed.search.search_sites'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'piston',
    'haystack',
    'wehaveweneed.web',
    'wehaveweneed.api',
    'wehaveweneed.search',
)

PAGINATE_POSTS_BY = 20

try:
    from local_settings import *
except ImportError:
    pass
