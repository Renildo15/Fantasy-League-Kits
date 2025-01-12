import pytest
from datetime import datetime, timezone
from championship_app.models import Championship

@pytest.mark.django_db
class TestChampionshipModel:
    """Testes para os métodos personalizados do modelo Championship."""

    @pytest.fixture
    def championship(self):
        """Cria uma instância de Championship."""
        return Championship.objects.create(
            name="Test Championship",
            logo_versions={
                "original": "http://example.com/media/original_logo.png",
                "512x512": "http://example.com/media/512x512_logo.png",
            },
        )
    
    def test_get_created_at_utc(self, championship):
        """Testa o método get_created_at_utc."""
        utc_created_at = championship.get_created_at_utc()
        assert utc_created_at == championship.created_at.astimezone(timezone.utc).isoformat()

    def test_get_updated_at_utc(self, championship):
        """Testa o método get_updated_at_utc."""
        utc_updated_at = championship.get_updated_at_utc()
        assert utc_updated_at == championship.updated_at.astimezone(timezone.utc).isoformat()

    def test_str(self, championship):
        """Testa o método __str__."""
        assert str(championship) == "Test Championship"