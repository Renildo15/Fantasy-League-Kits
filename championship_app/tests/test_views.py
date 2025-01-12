from datetime import timezone

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from ..models import Championship


@pytest.mark.django_db
class TestChampionshipListPublicView:
    """Testes para a view de listagem pública de campeonatos."""

    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def championships(self):
        return [
            Championship.objects.create(name="Championship 1"),
            Championship.objects.create(name="Championship 2"),
            Championship.objects.create(name="Championship 3"),
        ]

    def test_list_championships(self, api_client, championships):
        url = reverse("championships")
        response = api_client.get(url)
        assert response.status_code == 200

        expected_data = [
            {
                "id": str(championship.id),
                "name": championship.name,
                "logo_versions": championship.logo_versions,
            }
            for championship in championships
        ]

        response_data = response.json()["results"][0]

        response_data = response.json()["results"][0]
        response_data.pop("created_at", None)
        response_data.pop("updated_at", None)

        # Comparando os dados sem os campos de data
        expected_data[0].pop("created_at", None)
        expected_data[0].pop("updated_at", None)

        assert response_data == expected_data[0]


@pytest.mark.django_db
class TestChampionshipCreateView:
    """Testes para a view de criação de campeonato."""

    @pytest.fixture
    def api_client(self):
        return APIClient()

    def test_create_championship(self, api_client):
        url = reverse("create_championship")
        data = {"name": "Championship 1"}

        response = api_client.post(url, data=data)
        assert response.status_code == 201

        created_championship = Championship.objects.first()
        assert created_championship is not None
        assert created_championship.name == data["name"]


@pytest.mark.django_db
class TestChampionshipDetailPublicView:
    """Testes para a view de detalhes públicos de campeonato."""

    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def championship(self):
        return Championship.objects.create(name="Championship 1")

    def test_detail_championship(self, api_client, championship):
        url = reverse("championship", kwargs={"pk": championship.id})
        response = api_client.get(url)
        assert response.status_code == 200

        expected_data = {
            "id": str(championship.id),
            "name": championship.name,
            "logo_versions": championship.logo_versions,
        }

        response_data = response.json()
        response_data.pop("created_at", None)
        response_data.pop("updated_at", None)

        # Comparando os dados sem os campos de data
        expected_data.pop("created_at", None)
        expected_data.pop("updated_at", None)

        assert response_data == expected_data
