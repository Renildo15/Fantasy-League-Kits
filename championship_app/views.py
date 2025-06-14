from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.filters import SearchFilter
from django.db.models import Count

from .models import Championship
from title_app.models import Title
from club_app.models import Club
from .serializers import ChampionshipCreateSerializer, ChampionshipSerializer
from club_app.serializers import ClubWithTitlesSerializer

from django.db.models import Q


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

class ChampionshipChampionsView(generics.ListAPIView):
    serializer_class = ClubWithTitlesSerializer
    permission_classes = []
    filter_backends = [SearchFilter]
    search_fields = ["name"]

    def get_queryset(self):
        championship_slug = self.kwargs.get("championship_slug")
        championship = Championship.objects.filter(slug=championship_slug).first()

        if not championship:
            return Club.objects.none()
        
        champions_club = Club.objects.filter(
            titles__championship__slug=championship_slug
        ).annotate(
            num_titles=Count('titles', filter=Q(titles__championship__slug=championship_slug))
        ).order_by('-num_titles', 'name') 

        return champions_club