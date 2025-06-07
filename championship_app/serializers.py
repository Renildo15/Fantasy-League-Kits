from rest_framework import serializers

from .models import Championship


class ChampionshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Championship
        fields = "__all__"


class ChampionshipCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Championship
        fields = ["name", "logo", "table_image", "championship_type", "tier"]

    def create(self, validated_data):
        club = Championship.objects.create(**validated_data)
        return club
