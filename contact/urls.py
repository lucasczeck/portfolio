from django.urls import re_path
from contact import views

urlpatterns = [
    re_path('^get_infos$', views.GetContactInfos.as_view(), name='get_contact_infos'),
]
