from rest_framework import serializers
from .models import Stadium


class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = "__all__"


class CreateStadiumSerializer(serializers.ModelSerializer):

    def validate_name(self, value):

        if not value:
            raise serializers.ValidationError("This field cannot be blank.")

        if Stadium.objects.filter(name=value).exists():
            raise serializers.ValidationError("A stadium with this name already exists.")
        return value
    
    def validate_capacity(self, value):
        if value is not None and value <= 0:
            raise serializers.ValidationError("Capacity must be a positive integer.")
        
        if value <= 20000:
            raise serializers.ValidationError("Capacity must be greater than 20,000.")
        return value

    class Meta:
        model = Stadium
        fields = ["name", "capacity"]