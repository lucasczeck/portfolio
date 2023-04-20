import requests

from django.http import JsonResponse
from rest_framework.views import APIView

from BO.integrations.Github.Repository import Repository


class Repositories(APIView):
    def post(self, *args, **kwargs):
        url = 'https://api.github.com/users/lucasczeck/repos'
        response = requests.get(url)
        data = response.json()

        response = Repository(items=data).update_repositories()

        return JsonResponse(response, safe=False)


class Commit(APIView):
    def post(self, *args, **kwargs):
        urls = Repository.get_list_urls()


