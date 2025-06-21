from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny

from .models import Championship
from club_app.models import Club
from .serializers import ChampionshipCreateSerializer, ChampionshipSerializer
from club_app.serializers import ClubWithTitlesSerializer
from title_app.models import HistoryChampionship
from title_app.serializers import CreateHistoryChampionshipSerializer

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
            history_championship__championship__slug=championship_slug
        ).annotate(
            num_titles=Count('history_championship', filter=Q(history_championship__championship__slug=championship_slug))
        ).order_by('-num_titles', 'name') 

        return champions_club
    
class ChampionshipCreateChampionView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, championship_slug, club_uuid):
        championship = get_object_or_404(Championship, slug=championship_slug)
        club = get_object_or_404(Club, id=club_uuid)

        year = request.data.get('year', 30)

        if HistoryChampionship.objects.filter(championship=championship,year=year).exists():
            return Response({"detail": f"Já existe um campeão registrado para o ano {year}."},
                            status=status.HTTP_400_BAD_REQUEST)
        
        data = {
            "club": str(club.id),
            "championship": str(championship.id),
            "year": year,
            "coach": request.data.get("coach"),
            "captain": request.data.get("captain"),
            "runner_up": request.data.get("runner_up"),
            "top_scorer": request.data.get("top_scorer"),
            "top_scorer_goals": request.data.get("top_scorer_goals"),
            "top_assist": request.data.get("top_assist"),
            "top_assist_goals": request.data.get("top_assist_goals"),
            "top_goalkeeper": request.data.get("top_goalkeeper"),
            "top_goalkeeper_clean_sheets": request.data.get("top_goalkeeper_clean_sheets"),
        }

        serializer = CreateHistoryChampionshipSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)