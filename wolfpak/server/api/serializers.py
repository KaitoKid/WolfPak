from rest_framework import serializers

from .models import *


class QuestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quest
        fields = ["pk", "created_on", "completed_on", "x_coord", "y_coord",
         "message", "owner"]

class WolfSerializer(serializers.ModelSerializer):
    quests = QuestSerializer(many=True)

    class Meta:
        model = Wolf
        fields = ["pk", "first_name", "last_name", "quests"]


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