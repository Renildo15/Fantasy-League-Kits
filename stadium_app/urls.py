from django.urls import path
from .views import StadiumCreateView, StadiumListPublicView, StadiumDeleteView, StadiumDetailView, StadiumUpdateView

urlpatterns = [
    path("list/", StadiumListPublicView.as_view(), name="stadiums"),
    path("create/", StadiumCreateView.as_view(), name="create_stadium"),
    path("detail/<uuid:id>/", StadiumDetailView.as_view(), name="stadium_detail"),
    path("update/<uuid:id>/", StadiumUpdateView.as_view(), name="stadium_update"),
    path("delete/<uuid:id>/", StadiumDeleteView.as_view(), name="stadium_delete"),
]