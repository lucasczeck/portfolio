from django.urls import re_path

from dashboard import views

urlpatterns = [
    re_path('^cards$', views.GetCards.as_view(), name='get_cards')
]
