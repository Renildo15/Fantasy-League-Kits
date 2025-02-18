import os
from datetime import timezone
from io import BytesIO
from uuid import uuid4

from django.conf import settings
from django.core.files.base import ContentFile
from django.db import models
from PIL import Image

from io import BytesIO
import requests
# Create your models here.


class Championship(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="championships/logos/", null=True, blank=True)
    logo_versions = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Championship"
        verbose_name_plural = "Championships"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.logo:
            if settings.DEBUG:
                self.process_logos_versions_local()
            else:
                self.process_logos_versions_aws()
            super().save(update_fields=["logo_versions"])
            

    def process_logos_versions_local(self):
        original_path = self.logo.path
        resized_path = self.generate_resized_logo(original_path, (512, 512))

        original_url = f"{settings.SITE_DOMAIN}{settings.MEDIA_URL}{self.logo.name}"
        resized_url = f"{settings.SITE_DOMAIN}{settings.MEDIA_URL}{resized_path}"

        self.logo_versions = {
            "original": original_url,
            "512x512": resized_url,
        }

    def process_logos_versions_aws(self):
        original_url = f"{settings.MEDIA_URL}{self.logo.name}"  # Garante URL correta

        try:
            response = requests.get(original_url, timeout=10)  # Define um timeout
            response.raise_for_status()  # Verifica se o download falhou

            image_file = BytesIO(response.content)  # Armazena a imagem na memória
            resized_path = self.generate_resized_logo(image_file, (512, 512))

            resized_url = f"{settings.MEDIA_URL}{resized_path}"

            self.logo_versions = {
                "original": original_url,
                "512x512": resized_url,
            }
        except requests.exceptions.RequestException as e:
            print(f"Erro ao baixar a imagem do S3: {e}")

    def generate_resized_logo(self, original_path, size):

        from pathlib import Path

        with Image.open(original_path) as img:
            img = img.convert("RGBA")
            img.thumbnail(size, Image.LANCZOS)

            base, ext = os.path.splitext(Path(self.logo.name).name)
            resized_name = f"{base}_{size[0]}x{size[1]}{ext}"

            resized_path = Path(self.logo.field.upload_to) / resized_name

            buffer = BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)
            self.logo.storage.save(str(resized_path), ContentFile(buffer.read()))
            return str(resized_path)

    def __str__(self):
        return f"{self.name}"

    def get_created_at_utc(self):
        return self.created_at.astimezone(timezone.utc).isoformat()

    def get_updated_at_utc(self):
        return self.updated_at.astimezone(timezone.utc).isoformat()
