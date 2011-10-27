import os
import tempfile

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(tempfile.gettempdir(), 'naturalsortfield.sqlite'),
    }
}
INSTALLED_APPS = (
    'testproject.testapp',
)
