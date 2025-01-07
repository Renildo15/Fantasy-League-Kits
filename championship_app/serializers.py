from rest_framework import serializers

from .models import Championship


class ChampionshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Championship
        exclude = ("logo",)
