from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.filters import SearchFilter

from .models import Championship
from .serializers import ChampionshipCreateSerializer, ChampionshipSerializer


# Create your views here.
class ChampionshipListPublicView(generics.ListAPIView):
    queryset = Championship.objects.all().order_by("name")
    serializer_class = ChampionshipSerializer
    permission_classes = []
    filter_backends = [SearchFilter]
    search_fields = ["name", "championship_type", "tier"]


class ChampionshipCreateView(generics.CreateAPIView):
    queryset = Championship.objects.all()
    serializer_class = ChampionshipCreateSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = []


class ChampionshipDetailPublicView(generics.RetrieveAPIView):
    queryset = Championship.objects.all()
    serializer_class = ChampionshipSerializer
    permission_classes = []

class ChampionshipUpdateView(generics.UpdateAPIView):
    queryset = Championship.objects.all()
    serializer_class = ChampionshipCreateSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = []

class ChampionshipDeleteView(generics.DestroyAPIView):
    queryset = Championship.objects.all()
    serializer_class = ChampionshipSerializer
    permission_classes = []
    
    def perform_destroy(self, instance):
        instance.delete()
        return instance
    