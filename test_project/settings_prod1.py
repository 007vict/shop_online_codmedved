DEBUG = False
ALLOWED_HOSTS = ['*', '134.209.123.102']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db1',
        'USER': 'django_shop',
        'PASSWORD': 'django_shop',
        'HOST': 'localhost',
        'PORT': '',
    }
}