import os
import sys

path = '/home/YOUR_USERNAME/Alx_ecommerce_api'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'ecommerce_api.settings'
)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
