from django.http import JsonResponse
from rest_framework.views import APIView

from BO.contact.Info import Info


class GetContactInfos(APIView):

    @staticmethod
    def get(*args, **kwargs):
        contact_infos = Info.get_contact_infos()

        return JsonResponse(contact_infos, safe=False)
