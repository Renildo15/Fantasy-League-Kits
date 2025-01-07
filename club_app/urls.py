from django.urls import path

from .views import ClubDetailPublicView, ClubListPublicView

urlpatterns = [
    path("list/", ClubListPublicView.as_view(), name="clubs"),
    path("detail/<uuid:pk>/", ClubDetailPublicView.as_view(), name="club"),
]
