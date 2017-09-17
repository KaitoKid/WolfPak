from django.http import Http404, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist

from api.models import Quest
from api.serializers import QuestSerializer

class DDwightDetail(APIView):
    def post(self, request):
        q = Quest.objects.get(id=4)
        q.delete()
        return HttpResponse("Deleted Dwight")
