import pytest
from club_app.models import Club

@pytest.mark.django_db
class TestClubModels:
    """Testes para os métodos personalizados do modelo Club."""

    @pytest.fixture
    def club(self):
        return Club.objects.create(
            name="Test Club",
            emblem_versions={
                "original": "http://example.com/media/original_emblem.png",
                "512x512": "http://example.com/media/512x512_emblem.png",
            },
        )
    
    def test_str(self, club):
        assert str(club) == "Test Club"