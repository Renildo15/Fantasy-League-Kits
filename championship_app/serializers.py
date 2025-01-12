from rest_framework import serializers

from .models import Championship


class ChampionshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Championship
        exclude = ("logo",)


class ChampionshipCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Championship
        fields = ["name", "logo"]

    def create(self, validated_data):
        club = Championship.objects.create(**validated_data)
        return club
