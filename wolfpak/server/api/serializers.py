from rest_framework import serializers

from .models import *

class NeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Need
        fields = ["need"]

class QuestSerializer(serializers.ModelSerializer):
    needs = NeedSerializer(many=True)

    class Meta:
        model = Quest
        fields = ["pk", "name", "status", "created_on", "x_coord", "y_coord",
         "message", "needs"]

class WolfSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wolf
        fields = ["pk", "first_name", "last_name"]


class FamilySerializer(serializers.ModelSerializer):
    wolves = WolfSerializer(many=True)

    class Meta:
        model = Family
        fields = ["pk", "name", "family_type", "wolves"]


class PakSerializer(serializers.ModelSerializer):
    families = FamilySerializer(many=True)

    class Meta:
        model = Pak
        fields = ["pk", "name", "location", "families"]