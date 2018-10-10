"""
WSGI config for sharemyhealth project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
from .ssmenv import EC2ParameterStore

from django.core.wsgi import get_wsgi_application

try:
    parameter_store = EC2ParameterStore(region_name="us-east-1")
    # Automate env (dev)
    django_parameters = parameter_store.get_parameters_by_path(
        '/dev/sharemyhealth/',
        strip_path=True)
    EC2ParameterStore.set_env(django_parameters)
except Exception:
    pass

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sharemyhealth.settings')

application = get_wsgi_application()
