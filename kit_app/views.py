from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .models import Kit
from club_app.models import Club


class KitCurrentKitView(generics.UpdateAPIView):
    queryset = Kit.objects.all()
    permission_classes = []

    def get_club(self, club_id):
        return Club.objects.filter(id=club_id).first()

    def patch(self, request,club_id, *args, **kwargs):
        club = self.get_club(club_id)
        kit = self.get_queryset().filter(club=club).first()

        if not kit:
            return Response({"error": "Kit not found"}, status=status.HTTP_404_NOT_FOUND)
        
        kit.kit_current = not kit.kit_current
        kit.save()

        status_kit = "Current" if kit.kit_current else "Not current"

        return Response(
            {"message": f"Kit is {status_kit} successfully"},
            status=status.HTTP_200_OK
        )



