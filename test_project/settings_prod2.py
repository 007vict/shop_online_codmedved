DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_shop',
        'USER': 'django_shop',
        'PASSWORD': '1888vict',
        'HOST': 'localhost',
        'PORT': '',
    }
}