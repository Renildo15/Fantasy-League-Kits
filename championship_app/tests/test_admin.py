import pytest
from django.contrib.admin.sites import site
from championship_app.models import Championship
from championship_app.admin import ChampionshipAdmin

@pytest.mark.django_db
class TestChampionshipAdmin:
    """Testes para os métodos personalizados do admin."""

    @pytest.fixture
    def championship(self):
        """Cria uma instância de Championship com versões de logo."""
        return Championship.objects.create(
            name="Test Championship",
            logo_versions={
                "original": "http://example.com/media/original_logo.png",
                "512x512": "http://example.com/media/512x512_logo.png",
            },
        )
    
    @pytest.fixture
    def admin_instance(self):
        """Instância do admin."""
        return ChampionshipAdmin(model=Championship, admin_site=site)
    
    def test_logo_preview_no_logo(self, admin_instance):
        """Testa o método logo_preview quando não há logo."""
        championship = Championship.objects.create(name="Test Championship")
        result = admin_instance.logo_preview(championship)
        assert "No Logo" in result

    def test_clickable_logo_url_512(self, championship, admin_instance):
        """Testa o método clickable_logo_url_512."""
        result = admin_instance.clickable_logo_url_512(championship)
        assert (
            '<a href="http://example.com/media/512x512_logo.png"' in result
        )
        assert "target=\"_blank\"" in result

    def test_clickable_logo_url_no_url_512(self, admin_instance):
        """Testa o método clickable_logo_url_512."""
        championship = Championship.objects.create(name="Test Championship")
        result = admin_instance.clickable_logo_url_512(championship)
        assert result == "No URL"

    def test_clickable_logo_url(self, championship, admin_instance):
        """Testa o método clickable_logo_url."""
        result = admin_instance.clickable_logo_url(championship)
        assert (
                '<a href="http://example.com/media/original_logo.png"' in result
        )
        assert "target=\"_blank\"" in result

    def test_clickable_logo_url_no_url(self, admin_instance):
        """Testa o método clickable_logo_url."""
        championship = Championship.objects.create(name="Test Championship")
        result = admin_instance.clickable_logo_url(championship)
        assert result == "No URL"