from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist

from api.models import Wolf
from api.serializers import WolfSerializer

class WolfDetail(APIView):
    def get(self, request, wolf_id):
        try:
            wolf = Wolf.objects.get(pk=wolf_id)
        except ObjectDoesNotExist:
            raise Http404

        serializer = WolfSerializer(instance=wolf)
        return Response(serializer.data)

    def post(self, request, wolf_id):
        try:
            wolf = Wolf.objects.get(pk=wolf_id)
            serializer = WolfSerializer(wolf, request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data)
        except Wolf.DoesNotExist:
            wolf = Wolf(pk=wolf_id)
            serializer = WolfSerializer(wolf, request.data, partial=True)
            print(request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data)
