from django.urls import re_path

from aboutme import views

urlpatterns = [
    re_path('^personal_infos$', views.GetPersonalInfos.as_view(), name='get_personal_infos'),
    # re_path('^summary$', views.GetSummary.as_view(), name='get_summary'),
]
