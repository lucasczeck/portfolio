from django.urls import re_path

from core.admin import views

urlpatterns = [
    re_path('^login$', views.Login.as_view(), name='login'),
]
