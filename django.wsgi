import os, sys

path = '/home/kman/public_html'
if path not in sys.path:
    sys.path.insert(0, '/home/kman/public_html')

os.environ['DJANGO_SETTINGS_MODULE'] = 'drchrono.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
