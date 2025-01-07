from rest_framework import serializers

from .models import Kit


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
