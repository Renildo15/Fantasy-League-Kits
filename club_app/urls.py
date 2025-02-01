from django.urls import path

from .views import ClubCreateView, ClubDetailPublicView, ClubListPublicView, ClubRecentsListView

urlpatterns = [
    path("list/", ClubListPublicView.as_view(), name="clubs"),
    path("detail/<uuid:pk>/", ClubDetailPublicView.as_view(), name="club"),
    path("create/", ClubCreateView.as_view(), name="create_club"),
    path("recents/", ClubRecentsListView.as_view(), name="club_recents")
]
