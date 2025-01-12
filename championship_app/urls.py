from django.urls import path

from .views import (ChampionshipCreateView, ChampionshipDetailPublicView,
                    ChampionshipListPublicView)

urlpatterns = [
    path("list/", ChampionshipListPublicView.as_view(), name="championships"),
    path(
        "deatil/<uuid:pk>/", ChampionshipDetailPublicView.as_view(), name="championship"
    ),
    path("create/", ChampionshipCreateView.as_view(), name="create_championship"),
]
