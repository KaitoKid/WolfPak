from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist

from api.models import Quest
from api.serializers import QuestSerializer

class QuestDetail(APIView):
    def post(self, request, quest_id):
        try:
            quest = Quest.objects.get(pk=quest_id)
            serializer = QuestSerializer(quest, request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data)
        except Quest.DoesNotExist:
            quest = Quest(pk=quest_id)
            serializer = QuestSerializer(quest, request.data, partial=True)
            print(request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data)
