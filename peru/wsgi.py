"""
WSGI config for peru project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os, sys

# add the virtualenv site-packages path to the sys.path
site_packages = '/home/rafaelolal/envs/peru_env/lib/python3.10/site-packages'
if site_packages not in sys.path:
    sys.path.append(site_packages)

project_path = '/home/rafaelolal/peru'
project_path2 = '/home/rafaelolal/peru/peru'

if project_path not in sys.path:
    sys.path.append(project_path)
if project_path2 not in sys.path:
    sys.path.append(project_path2)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'peru.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
