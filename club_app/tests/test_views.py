import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from club_app.models import Club

@pytest.mark.django_db
class TestClubViews:
    """Testes para a view de listagem pública dos clubes."""

    @pytest.fixture
    def api_client(self):
        return APIClient()
     
    @pytest.fixture
    def clubs(self):
        return [
            Club.objects.create(name="Club 1"),
            Club.objects.create(name="Club 2"),
            Club.objects.create(name="Club 3"),
        ]
     
    def test_list_clubs(self, api_client, clubs):
        url = reverse("clubs")
        response = api_client.get(url)
        assert response.status_code == 200

        expected_data = [
            {
                "id": str(club.id),
                "kits":[],
                "name": club.name,
                "emblem_versions": club.emblem_versions,
            }
            for club in clubs
         ]

        response_data = response.json()["results"][0]
        response_data.pop("created_at", None)
        response_data.pop("updated_at", None)

        # Comparando os dados sem os campos de data
        expected_data[0].pop("created_at", None)
        expected_data[0].pop("updated_at", None)

        assert response_data == expected_data[0]



@pytest.mark.django_db
class TestClubCreateView:
    """Testes para a view de criação de clube."""

    @pytest.fixture
    def api_client(self):
        return APIClient()
    
    def test_create_club(self, api_client):
        url = reverse("create_club")
        data = {"name": "Club 1"}

        response = api_client.post(url, data=data)
        assert response.status_code == 201

        club = Club.objects.first()
        assert club is not None
        assert club.name == data["name"]

@pytest.mark.django_db
class TestClubDetailView:
    """Testes para a view de detalhes públicos do clube."""

    @pytest.fixture
    def api_client(self):
        return APIClient()
    
    @pytest.fixture
    def club(self):
        return Club.objects.create(name="Club 1")
    
    def test_club_detail(self, api_client, club):
        url = reverse("club", kwargs={"pk": club.id})
        response = api_client.get(url)
        assert response.status_code == 200

        expected_data = {
            "id": str(club.id),
            "kits":[],
            "name": club.name,
            "emblem_versions": club.emblem_versions,
        }

        response_data = response.json()
        response_data.pop("created_at", None)
        response_data.pop("updated_at", None)

        # Comparando os dados sem os campos de data
        expected_data.pop("created_at", None)
        expected_data.pop("updated_at", None)

        assert response_data == expected_data