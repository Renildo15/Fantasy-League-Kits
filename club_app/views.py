from rest_framework import generics
from rest_framework.filters import SearchFilter

from .models import Club
from .serializers import ClubCreateSerializer, ClubSerializer


# Create your views here.
class ClubListPublicView(generics.ListAPIView):
    queryset = Club.objects.all().order_by("name")
    serializer_class = ClubSerializer
    permission_classes = []
    filter_backends = [SearchFilter]
    search_fields = ["name"]


class ClubCreateView(generics.CreateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubCreateSerializer
    permission_classes = []


class ClubDetailPublicView(generics.RetrieveAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    permission_classes = []
