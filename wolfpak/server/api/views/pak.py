from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist

from api.models import Pak
from api.serializers import PakSerializer

class PakDetail(APIView):
    def get(self, request, pak_id):
        try:
            pak = Pak.objects.get(pk=pak_id)
        except ObjectDoesNotExist:
            raise Http404

        serializer = PakSerializer(instance=pak)
        return Response(serializer.data)

    def post(self, request, pak_id):
        try:
            pak = Pak.objects.get(pk=pak_id)
            serializer = PakSerializer(pak, request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data)
        except Pak.DoesNotExist:
            pak = Pak(pk=pak_id)
            serializer = PakSerializer(pak, request.data, partial=True)
            print(request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data)
