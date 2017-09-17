from django.http import Http404, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
import os
from api.models import Quest
from api.models import Need
from api.serializers import QuestSerializer

class ReceiveDetail(APIView):
    def get(self, request):
        # SEND A TEXT
        '''
        url = "https://rest.nexmo.com/sms/json"
        data = {"api_key":"2356ce2f", "api_secret": "0938509e385aca57", "to":"15102068793", "from":"12016728806",
                "text": "HELLO AGAIN"}
        '''

        # EDIT THE 'TO' FOR WHOEVER IS SENDING A TEXT
        os.system("curl -X POST  https://rest.nexmo.com/sms/json \
        -d api_key=2356ce2f \
        -d api_secret=0938509e385aca57 \
        -d to=15105291564 \
        -d from=12016728806 \
        -d text='Hey Dwight, we received your request. Someone will assist you soon.'")

        q = Quest(id=4, name="Dwight", status=0, created_on="2019-09-16 00:19:54", latitude=37.7581836, longitude=-122.3899936,
                  message="Has a big beard and wearing blue jeans")
        q.save()
        n = Need(need=3, owner=q)
        n.save()
        n3 = Need(need=6, owner=q)
        n3.save()

        serializer = QuestSerializer(instance=q)
        return Response(serializer.data)
