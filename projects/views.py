from django.http import JsonResponse
from rest_framework.views import APIView

from BO.projects.Repository import Repository
from BO.projects.Project import Project


class GetRepositoriesView(APIView):

    @staticmethod
    def get(*args, **kwargs):
        repositories = Repository.get_pending_repositories()

        return JsonResponse(repositories, safe=False)


class GetProjectsView(APIView):

    @staticmethod
    def get(*args, **kwargs):
        projects = Project.get_all_projects()

        return JsonResponse(projects, safe=False)


class ProjectView(APIView):

    def get(self, *args, **kwargs):
        project_id = self.request.GET.get('project_id')

        project = Project(id=project_id).get_project()

        return JsonResponse(project, safe=False)

    def post(self, *args, **kwargs):
        project_id = self.request.POST.get('project_id')

        project = Project(id=project_id).save_project()

