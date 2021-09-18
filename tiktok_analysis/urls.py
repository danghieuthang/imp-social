from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('verify-user', views.verify_titok_user),
]

urlpatterns = format_suffix_patterns(urlpatterns)