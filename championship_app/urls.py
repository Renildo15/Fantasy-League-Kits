from django.urls import path

from .views import (ChampionshipCreateView, ChampionshipDetailPublicView,
                    ChampionshipListPublicView, ChampionshipUpdateView, ChampionshipDeleteView, ChampionshipChampionsView)

urlpatterns = [
    path("list/", ChampionshipListPublicView.as_view(), name="championships"),
    path(
        "detail/<uuid:pk>/", ChampionshipDetailPublicView.as_view(), name="championship"
    ),
    path("create/", ChampionshipCreateView.as_view(), name="create_championship"),
    path("update/<uuid:pk>/", ChampionshipUpdateView.as_view(), name="update_championship"),
    path("delete/<uuid:pk>/", ChampionshipDeleteView.as_view(), name="delete_championship"),
    path("champions/<slug:championship_slug>/", ChampionshipChampionsView.as_view(), name="championship_champions"),
]
