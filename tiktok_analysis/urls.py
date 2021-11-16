from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('verify-user', views.verify_titok_user),
    path('summary-post', views.get_summary_post),
    path('get-user', views.get_user),
    path('get-list-post', views.get_items_of_user),
]

urlpatterns = format_suffix_patterns(urlpatterns)
