from django.http import JsonResponse
from rest_framework.views import APIView

from BO.projects.Repository import Repository


class GetRepositories(APIView):

    @staticmethod
    def get(*args, **kwargs):
        repositories = Repository.get_pending_repositories()

        return JsonResponse(repositories, safe=False)


class GetProjects(APIView):

    @staticmethod
    def get(*args, **kwargs):
        pass