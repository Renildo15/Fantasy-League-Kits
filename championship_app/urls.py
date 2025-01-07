from django.urls import path

from .views import ChampionshipDetailPublicView, ChampionshipListPublicView

urlpatterns = [
    path("list/", ChampionshipListPublicView.as_view(), name="championships"),
    path(
        "deatil/<uuid:pk>/", ChampionshipDetailPublicView.as_view(), name="championship"
    ),
]
