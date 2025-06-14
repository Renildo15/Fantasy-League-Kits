from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Club
from .serializers import ClubCreateSerializer, ClubSerializer


# Create your views here.
class ClubListPublicView(generics.ListAPIView):
    serializer_class = ClubSerializer
    permission_classes = []
    filter_backends = [SearchFilter]
    search_fields = ["name"]

    def get_queryset(self):
        queryset = Club.objects.all().order_by("name")
        federation = self.request.query_params.get("federation", None)
        if federation:
            queryset = queryset.filter(federation=federation)
        return queryset

class ClubRecentsListView(generics.ListAPIView):
    queryset = Club.objects.all().order_by("-created_at")[:5]
    serializer_class = ClubSerializer
    permission_classes = []

class ClubCreateView(generics.CreateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubCreateSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = []


class ClubDetailPublicView(generics.RetrieveAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    permission_classes = []