import pytest
from django.contrib.admin.sites import site
from club_app.models import Club
from club_app.admin import ClubAdmin

@pytest.mark.django_db
class TestClubAdmin:
    """Testes para os métodos personalizados do admin."""

    @pytest.fixture
    def club(self):
        return Club.objects.create(
            name="Test Club",
            emblem_versions={
                "original": "http://example.com/media/original_emblem.png",
                "512x512": "http://example.com/media/512x512_emblem.png",
            },
        )
    
    @pytest.fixture
    def admin_instance(self):
        return ClubAdmin(model=Club, admin_site=site)
    
    def test_emblem_preview_no_emblem(self, admin_instance):
        club = Club.objects.create(name="Test Club")
        result = admin_instance.emblem_preview(club)
        assert "No Emblem" in result

    def test_clickable_emblem_url_512(self, club, admin_instance):
        result = admin_instance.clickable_emblem_url_512(club)
        assert (
            '<a href="http://example.com/media/512x512_emblem.png"' in result
        )
        assert "target=\"_blank\"" in result

    def test_clickable_emblem_url_no_url_512(self, admin_instance):
        club = Club.objects.create(name="Test Club")
        result = admin_instance.clickable_emblem_url_512(club)
        assert result == "No Emblem"

    def test_clickable_emblem_url(self, club, admin_instance):
        result = admin_instance.clickable_emblem_url_original(club)
        assert (
                '<a href="http://example.com/media/original_emblem.png"' in result
        )
        assert "target=\"_blank\"" in result

    def test_clickable_emblem_url_no_url(self, admin_instance):
        club = Club.objects.create(name="Test Club")
        result = admin_instance.clickable_emblem_url_original(club)
        assert result == "No Emblem"
        