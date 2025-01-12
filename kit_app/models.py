from uuid import uuid4

from django.conf import settings
from django.db import models


# Create your models here.
class Kit(models.Model):

    KIT_TYPE_CHOICES = (
        ("fts", "FTS"),
        ("fl", "FL"),
        ("dls", "DLS"),
        ("other", "Other"),
    )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    club = models.ForeignKey(
        "club_app.Club", on_delete=models.CASCADE, related_name="kits"
    )
    kit_home = models.ImageField(upload_to="kits/home/", null=True, blank=True)
    kit_home_url = models.URLField(null=True, blank=True)
    kit_away = models.ImageField(upload_to="kits/away/", null=True, blank=True)
    kit_away_url = models.URLField(null=True, blank=True)
    kit_goalkeeper_home = models.ImageField(
        upload_to="kits/home/", null=True, blank=True
    )
    kit_goalkeeper_home_url = models.URLField(null=True, blank=True)
    kit_goalkeeper_away = models.ImageField(
        upload_to="kits/away/", null=True, blank=True
    )
    kit_goalkeeper_away_url = models.URLField(null=True, blank=True)
    kit_version = models.CharField(max_length=255, null=True, blank=True)
    kit_current = models.BooleanField(default=False)
    kit_type = models.CharField(max_length=255, choices=KIT_TYPE_CHOICES, default="fts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Kit"
        verbose_name_plural = "Kits"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.kit_home and not self.kit_home_url:
            full_url = f"{settings.SITE_DOMAIN}{settings.MEDIA_URL}{self.kit_home.name}"
            self.kit_home_url = full_url
            super().save(update_fields=["kit_home_url"])

        if self.kit_away and not self.kit_away_url:
            full_url = f"{settings.SITE_DOMAIN}{settings.MEDIA_URL}{self.kit_away.name}"
            self.kit_away_url = full_url
            super().save(update_fields=["kit_away_url"])

        if self.kit_goalkeeper_home and not self.kit_goalkeeper_home_url:
            full_url = f"{settings.SITE_DOMAIN}{settings.MEDIA_URL}{self.kit_goalkeeper_home.name}"
            self.kit_goalkeeper_home_url = full_url
            super().save(update_fields=["kit_goalkeeper_home_url"])

        if self.kit_goalkeeper_away and not self.kit_goalkeeper_away_url:
            full_url = f"{settings.SITE_DOMAIN}{settings.MEDIA_URL}{self.kit_goalkeeper_away.name}"
            self.kit_goalkeeper_away_url = full_url
            super().save(update_fields=["kit_goalkeeper_away_url"])
