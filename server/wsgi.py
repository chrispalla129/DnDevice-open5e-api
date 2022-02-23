"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os, sys
# add the hellodjango project path into the sys.path

# add the virtualenv site-packages path to the sys.path
sys.path.append('/root/.local/share/virtualenvs/open5e-api-GCOA7Kjv/lib/python3.7/site-packages/')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

application = get_wsgi_application()
