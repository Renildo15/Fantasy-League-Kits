from rest_framework import serializers

from .models import Club

from stadium_app.serializers import StadiumSerializer


class ClubSerializer(serializers.ModelSerializer):
    stadium = StadiumSerializer(read_only=True)
    class Meta:
        model = Club
        fields = "__all__"

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     if self.context.get("all_kits", False):
    #         representation["kits"] = KitSerializer(instance.kits.all(), many=True).data
    #     else:
    #         current_kit = instance.kits.filter(kit_current=True).first()
    #         if current_kit:
    #             representation["kits"] = KitSerializer(current_kit).data
    #         else:
    #             representation["kits"] = []

    #     return representation


class ClubCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ["name", "federation", "emblem", "abbreviation", "stadium", "coach"]

    def create(self, validated_data):
        abbreviation = validated_data.get("abbreviation", "").upper()
        validated_data["abbreviation"] = abbreviation
        club = Club.objects.create(**validated_data)
        return club
