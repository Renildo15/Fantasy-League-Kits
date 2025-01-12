import os
from io import BytesIO
from uuid import uuid4

from django.conf import settings
from django.core.files.base import ContentFile
from django.db import models
from PIL import Image


# Create your models here.
class Club(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    emblem = models.ImageField(upload_to="clubs/emblems/", null=True, blank=True)
    emblem_versions = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Club"
        verbose_name_plural = "Clubs"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.emblem:
            self.process_emblem_versions()
            super().save(update_fields=["emblem_versions"])

    def process_emblem_versions(self):
        original_path = self.emblem.path
        resized_path = self.generate_resized_emblem(original_path, (512, 512))

        original_url = f"{settings.SITE_DOMAIN}{settings.MEDIA_URL}{self.emblem.name}"
        resized_url = f"{settings.SITE_DOMAIN}{settings.MEDIA_URL}{resized_path}"

        self.emblem_versions = {
            "original": original_url,
            "512x512": resized_url,
        }

    def generate_resized_emblem(self, original_path, size):

        from pathlib import Path

        with Image.open(original_path) as img:
            img = img.convert("RGBA")
            img.thumbnail(size, Image.LANCZOS)

            base, ext = os.path.splitext(Path(self.emblem.name).name)
            resized_name = f"{base}_{size[0]}x{size[1]}{ext}"

            resized_path = Path(self.emblem.field.upload_to) / resized_name

            buffer = BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)
            self.emblem.storage.save(str(resized_path), ContentFile(buffer.read()))
            return str(resized_path)

    def __str__(self):
        return f"{self.name}"
