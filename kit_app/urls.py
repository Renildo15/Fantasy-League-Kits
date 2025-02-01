from django.urls import path

from .views import KitCurrentKitView

urlpatterns = [
    path("current/<uuid:club_id>", KitCurrentKitView.as_view(), name="kit_current"),
]
