from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist

from api.models import Quest
from api.serializers import QuestSerializer

class ReceiveDetail(APIView):
    def post(self, request):
        quest = Quest()
        serializer = QuestSerializer(quest, request.data, partial=True)
        print(request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
