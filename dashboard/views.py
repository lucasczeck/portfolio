from django.http import JsonResponse
from rest_framework.views import APIView

from BO.dashboard.Cards import Cards
from BO.dashboard.Summary import Summary


class GetCards(APIView):
    def get(self, *args, **kwargs):
        response = Cards().get_cards()

        return JsonResponse(response, safe=False)


class GetSummary(APIView):
    def get(self, *args, **kwargs):
        response = Summary().get_summary()

        return JsonResponse(response, safe=False)
