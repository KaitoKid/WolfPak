from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist

from api.models import Quest
from api.serializers import QuestSerializer

class AllQuestsDetail(APIView):
    def get(self, request):
        quest = Quest.objects.all()
        serializer = QuestSerializer(instance=quest, many=True)
        return Response(serializer.data)