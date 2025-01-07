from uuid import uuid4

from django.conf import settings
from django.db import models

# Create your models here.


class Championship(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="championships/logos/", null=True, blank=True)
    logo_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Championship"
        verbose_name_plural = "Championships"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.logo and not self.logo_url:
            full_url = f"{settings.SITE_DOMAIN}{settings.MEDIA_URL}{self.logo.name}"
            breakpoint()
            self.logo_url = full_url
            super().save(update_fields=["logo_url"])

    def __str__(self):
        return f"{self.name} - {self.logo_url}"
