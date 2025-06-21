from rest_framework import serializers
from .models import HistoryChampionship

class CreateHistoryChampionshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryChampionship
        fields = "__all__"
        read_only_fields = ['id', 'created_at', 'updated_at']

class HistoryChampionshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryChampionship
        fields = "__all__"

class HistoryChampionshipWrappedSerializer(serializers.ModelSerializer):
    info = serializers.SerializerMethodField()

    class Meta:
        model = HistoryChampionship
        fields = ['year', 'info']

    def get_info(self, obj):
        data = HistoryChampionshipSerializer(obj).data
        data.pop("year", None)
        return data