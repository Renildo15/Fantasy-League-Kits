from rest_framework import serializers

from kit_app.serializers import KitSerializer

from .models import Club


class ClubSerializer(serializers.ModelSerializer):
    kits = KitSerializer(many=True, read_only=True)

    class Meta:
        model = Club
        exclude = ("emblem",)
