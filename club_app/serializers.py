from rest_framework import serializers

from kit_app.serializers import KitSerializer

from .models import Club


class ClubSerializer(serializers.ModelSerializer):
    kits = KitSerializer(many=True, read_only=True)

    class Meta:
        model = Club
        exclude = ("emblem",)


class ClubCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ["name", "emblem"]

    def create(self, validated_data):
        club = Club.objects.create(**validated_data)
        return club
