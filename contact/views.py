from django.http import JsonResponse
from rest_framework.views import APIView


class GetContactInfos(APIView):
    def get(self, *args, **kwargs):
