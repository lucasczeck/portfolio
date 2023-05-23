from django.urls import re_path

from dashboard import views

urlpatterns = [
    re_path('^personal_infos$', views.GetCards.as_view(), name='get_cards'),
    re_path('^summary$', views.GetSummary.as_view(), name='get_summary'),
]
