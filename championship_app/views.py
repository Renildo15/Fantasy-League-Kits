from rest_framework import generics
from rest_framework.filters import SearchFilter

from .models import Championship
from .serializers import ChampionshipSerializer, ChampionshipCreateSerializer


# Create your views here.
class ChampionshipListPublicView(generics.ListAPIView):
    queryset = Championship.objects.all()
    serializer_class = ChampionshipSerializer
    permission_classes = []
    filter_backends = [SearchFilter]
    search_fields = ["name"]

class ChampionshipCreateView(generics.CreateAPIView):
    queryset = Championship.objects.all()
    serializer_class = ChampionshipCreateSerializer
    permission_classes = []


class ChampionshipDetailPublicView(generics.RetrieveAPIView):
    queryset = Championship.objects.all()
    serializer_class = ChampionshipSerializer
    permission_classes = []
