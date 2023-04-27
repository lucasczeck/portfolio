from django.http import JsonResponse
from rest_framework.views import APIView

from BO.dashboard.Cards import Cards


class GetCards(APIView):

    def get(self, *args, **kwargs):
        response = Cards().get_cards()

        return JsonResponse(response, safe=False)
