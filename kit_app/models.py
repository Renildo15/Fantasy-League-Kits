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
        super().save(*args, **kwargs)  # Primeiro salva o objeto

        updated_fields = []  # Lista para rastrear quais campos precisam ser atualizados

        def set_url(image_field, url_field):
            """Define a URL do kit, dependendo do ambiente (DEBUG ou Produção)."""
            image = getattr(self, image_field)
            if image and not getattr(self, url_field):
                if settings.DEBUG:
                    full_url = f"{settings.SITE_DOMAIN}{settings.MEDIA_URL}{image.name}"
                else:
                    full_url = f"{settings.MEDIA_URL}{image.name}"

                setattr(self, url_field, full_url)
                updated_fields.append(url_field)

        set_url("kit_home", "kit_home_url")
        set_url("kit_away", "kit_away_url")
        set_url("kit_goalkeeper_home", "kit_goalkeeper_home_url")
        set_url("kit_goalkeeper_away", "kit_goalkeeper_away_url")

        if updated_fields:  # Só faz um novo save se houver algo para atualizar
            super().save(update_fields=updated_fields)

