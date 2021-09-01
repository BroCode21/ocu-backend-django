from django.urls.conf import path
from .views import login


urlpatterns = [
    path("login/", login),
]
