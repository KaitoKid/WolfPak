from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
import os

from api.models import Quest
from api.serializers import QuestSerializer

class QuestDetail(APIView):
    def post(self, request, quest_id):
        os.system("curl -X POST  https://rest.nexmo.com/sms/json \
        -d api_key=2356ce2f \
        -d api_secret=0938509e385aca57 \
        -d to=15105291564 \
        -d from=12016728806 \
        -d text='Hey Dwight, help is on the way! Hang tight!'")
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
