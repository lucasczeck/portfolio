from django.urls import path

from core.integracoes.github import views

urlpatterns = [
    path('commits', views.Commit.as_view(), name='commits')
]