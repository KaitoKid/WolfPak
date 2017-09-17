from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist

from api.models import Need
from api.serializers import NeedSerializer

class NeedDetail(APIView):
    def get(self, reneed, need_id):
        try:
            need = Need.objects.get(pk=need_id)
        except ObjectDoesNotExist:
            raise Http404

        serializer = NeedSerializer(instance=need)
        return Response(serializer.data)

    def post(self, reneed, need_id):
        try:
            need = Need.objects.get(pk=need_id)
            serializer = NeedSerializer(need, reneed.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data)
        except Need.DoesNotExist:
            need = Need(pk=need_id)
            serializer = NeedSerializer(need, reneed.data, partial=True)
            print(reneed.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data)
