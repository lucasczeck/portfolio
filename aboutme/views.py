from django.http import JsonResponse
from rest_framework.views import APIView

import BO.aboutme.Personal


class GetPersonalInfos(APIView):
    def get(self, *args, **kwargs):
        personal_infos = BO.aboutme.Personal.PersonalInfos().get_personal_infos()

        return JsonResponse(personal_infos, safe=False)
