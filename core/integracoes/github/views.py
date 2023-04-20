import requests

from django.http import JsonResponse
from rest_framework.views import APIView


class Repositories(APIView):
    def post(self, *args, **kwargs):
        url = 'https://api.github.com/users/lucasczeck/repos'
        response = requests.get(url)
        data = response.json()


class Commit(APIView):
    def get(self, *args, **kwargs):
        pass
