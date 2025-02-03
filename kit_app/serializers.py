from rest_framework import serializers

from .models import Kit
from club_app.models import Club


class KitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kit
        exclude = (
            "club",
            "kit_home",
            "kit_away",
            "kit_goalkeeper_home",
            "kit_goalkeeper_away",
        )

class KitCurrentKitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kit
        fields = ["kit_current"]
class KitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kit
        fields = [
            "club",
            "kit_home",
            "kit_away",
            "kit_goalkeeper_home",
            "kit_goalkeeper_away",
            "kit_version",
            "kit_current",
            "kit_type"
        ]

    