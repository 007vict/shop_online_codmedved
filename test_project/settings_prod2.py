DEBUG = False
ALLOWED_HOSTS = ['*', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test_project',
        'USER': 'django_shop',
        'PASSWORD': '1888vict',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}