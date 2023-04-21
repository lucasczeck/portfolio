from django.urls import re_path

from core.integracoes.github import views

urlpatterns = [
    re_path('^repositories$', views.Repositories.as_view(), name='commits'),
    re_path('^commits$', views.Commits.as_view(), name='commits'),
]
