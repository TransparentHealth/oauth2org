from django.conf.urls import url
from .views import oauth_authorization_server


urlpatterns = [
    # openid-configuration -----------------------------------
    url(r'^oauth-authorization-server$',
        oauth_authorization_server,
        name='oauth_authorization_server'),
]
