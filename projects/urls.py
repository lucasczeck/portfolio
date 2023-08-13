from django.urls import re_path
from projects import views

urlpatterns = [
    re_path('^get_repositories$', views.GetRepositoriesView.as_view(), name='get_repositories'),
    re_path('^get_projects$', views.GetProjectsView.as_view(), name='get_projects'),
    re_path('^project$', views.ProjectView.as_view(), name='project'),
    re_path('^get_list_projects$', views.ListProjectView.as_view(), name='get_list_projects'),
]
