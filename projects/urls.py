from django.urls import re_path
from projects import views

urlpatterns = [
    re_path('^get_repositories$', views.GetRepositories.as_view(), name='get_repositories'),
    re_path('^get_project$', views.GetProjects.as_view(), name='get_projects'),
]
