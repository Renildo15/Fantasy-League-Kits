from rest_framework import generics

from  .models import Stadium
from .serializers import StadiumSerializer, CreateStadiumSerializer

class StadiumListPublicView(generics.ListAPIView):
    serializer_class = StadiumSerializer
    permission_classes = []
    filter_backends = []
    search_fields = ["name"]

    def get_queryset(self):
        queryset = Stadium.objects.all().order_by("name")
        return queryset
    

class StadiumCreateView(generics.CreateAPIView):
    queryset = Stadium.objects.all()
    serializer_class = CreateStadiumSerializer
    permission_classes = []


class StadiumDetailView(generics.RetrieveAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = []
    lookup_field = "id"

class StadiumUpdateView(generics.UpdateAPIView):
    queryset = Stadium.objects.all()
    serializer_class = CreateStadiumSerializer
    permission_classes = []
    lookup_field = "id"

class StadiumDeleteView(generics.DestroyAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = []
    lookup_field = "id"

    def perform_destroy(self, instance):
        instance.delete()
        return instance