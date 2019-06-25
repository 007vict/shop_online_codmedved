DEBUG = False
ALLOWED_HOSTS = ['*', '134.209.123.102']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djashopmedv',
        'USER': 'djles_db',
        'PASSWORD': '1888vict',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}