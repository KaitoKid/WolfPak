from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist

from api.models import Family
from api.serializers import FamilySerializer

class FamilyDetail(APIView):
    def get(self, request, family_id):
        try:
            family = Family.objects.get(pk=family_id)
        except ObjectDoesNotExist:
            raise Http404

        serializer = FamilySerializer(instance=family)
        return Response(serializer.data)

    def post(self, request, pak_id):
        try:
            pak = Family.objects.get(pk=pak_id)
            serializer = FamilySerializer(pak, request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data)
        except Family.DoesNotExist:
            pak = Family(pk=pak_id)
            serializer = FamilySerializer(pak, request.data, partial=True)
            print(request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data)
