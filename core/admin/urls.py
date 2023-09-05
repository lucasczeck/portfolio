from django.urls import re_path

from core.admin import views

urlpatterns = [
    re_path('^login$', views.Login.as_view(), name='login'),
    re_path('^get_cards$', views.GetCardsAdmin.as_view(), name='get_cards_admin')
]
