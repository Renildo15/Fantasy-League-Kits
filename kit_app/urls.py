from django.urls import path

from .views import KitCurrentKitView, KitCreateView

urlpatterns = [
    path("current/<uuid:kit_id>", KitCurrentKitView.as_view(), name="kit_current"),
    path("create/",KitCreateView.as_view(), name="kit_create" )
]
