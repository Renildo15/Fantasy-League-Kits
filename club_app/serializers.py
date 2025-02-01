from rest_framework import serializers

from kit_app.serializers import KitSerializer

from .models import Club


class ClubSerializer(serializers.ModelSerializer):
    kits = KitSerializer(many=True, read_only=True)

    class Meta:
        model = Club
        exclude = ("emblem",)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.context.get("all_kits", False):
            representation["kits"] = KitSerializer(instance.kits.all(), many=True).data
        else:
            current_kit = instance.kits.filter(kit_current=True).first()
            if current_kit:
                representation["kits"] = KitSerializer(current_kit).data
            else:
                representation["kits"] = []

        return representation


class ClubCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ["name", "federation", "emblem"]

    def create(self, validated_data):
        club = Club.objects.create(**validated_data)
        return club
