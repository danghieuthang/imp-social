from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('get-post', views.get_post),
]

urlpatterns = format_suffix_patterns(urlpatterns)
