from uuid import uuid4

from django.conf import settings
from django.db import models


# Create your models here.
class Club(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    emblem = models.ImageField(upload_to="clubs/emblems/", null=True, blank=True)
    emblem_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Club"
        verbose_name_plural = "Clubs"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.emblem and not self.emblem_url:
            full_url = f"{settings.SITE_DOMAIN}{settings.MEDIA_URL}{self.emblem.name}"
            self.emblem_url = full_url
            super().save(update_fields=["emblem_url"])

    def __str__(self):
        return f"{self.name}"
