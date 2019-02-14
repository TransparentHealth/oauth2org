

# Copyright Videntity Systems, Inc.
from django.conf.urls import url
from .views.core import (account_settings, )
from .views.oauth2_profile import userinfo_test

urlpatterns = [
    url(r'^settings', account_settings, name='account_settings'),
    url(r'^userinfo', userinfo_test, name='userinfo_test'),
]
