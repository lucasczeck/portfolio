from django.http import JsonResponse
from rest_framework.views import APIView


class Commit(APIView):
    def get(self, *args, **kwargs):
        pass