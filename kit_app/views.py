from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .models import Kit


class KitCurrentKitView(generics.UpdateAPIView):
    queryset = Kit.objects.all()
    permission_classes = []


    def patch(self, request,kit_id, *args, **kwargs):
        kit = self.get_queryset().filter(id=kit_id).first()

        if not kit:
            return Response({"error": "Kit not found"}, status=status.HTTP_404_NOT_FOUND) 
        club = kit.club
        active_kits = club.kits.filter(kit_current=True).exclude(id=kit_id)

        if active_kits.exists():
            for active_kit in active_kits:
                active_kit.kit_current = False
                active_kit.save()

        kit.kit_current = not kit.kit_current
        kit.save()

        status_kit = "current" if kit.kit_current else "not current"

        return Response(
            {"message": f"Kit {status_kit}"},
            status=status.HTTP_200_OK,
        )
