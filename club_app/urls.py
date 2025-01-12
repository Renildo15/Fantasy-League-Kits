from django.urls import path

from .views import ClubCreateView, ClubDetailPublicView, ClubListPublicView

urlpatterns = [
    path("list/", ClubListPublicView.as_view(), name="clubs"),
    path("detail/<uuid:pk>/", ClubDetailPublicView.as_view(), name="club"),
    path("create/", ClubCreateView.as_view(), name="create_club"),
]
