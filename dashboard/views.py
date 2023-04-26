from django.http import JsonResponse
from rest_framework.views import APIView

from BO.utils.Date import Date
from BO.dashboard.Cards import Cards


class GetCards(APIView):

    def get(self, *args, **kwargs):
        today = Date.get_today_date()

        response = Cards(date=today).get_cards()

        return JsonResponse(response, safe=False)
