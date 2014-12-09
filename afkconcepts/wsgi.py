"""
WSGI config for tango_with_django_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""
##For Virutal Hosting
import sys
path = sys.path[0]
if path not in sys.path:
    sys.path.append(path)

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "afkconcepts.settings")
#os.environ["DJANGO_SETTINGS_MODULE"] = "afkconcepts.settings"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
