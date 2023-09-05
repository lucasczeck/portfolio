from django.http import JsonResponse
from rest_framework.views import APIView

import BO.admin.cards


class Login(APIView):
    def post(self, *args, **kwargs):
        username = self.request.data.get('username')
        password = self.request.data.get('password')

        response = {'status': True, 'msg': 'erro'}

        return JsonResponse(response, safe=False)


class GetCardsAdmin(APIView):

    def get(self, *args, **kwargs):
        cards = BO.admin.cards.CardsAdmin().get_cards()

        return JsonResponse(cards, safe=False)
