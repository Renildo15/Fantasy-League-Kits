from datetime import timezone
from uuid import uuid4

from django.core.files.base import ContentFile
from django.db import models

# Create your models here.


class Championship(models.Model):
    CHAMPIONSHIP_TYPES = [
        ('LEAGUE', 'League'),
        ('KNOCKOUT', 'Knockout'),
        ('GROUP_KNOCKOUT', 'Group Stage + Knockout'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    logo = models.ImageField(upload_to="championships/logos/", null=True, blank=True)
    table_image = models.ImageField(upload_to="championships/tables/", null=True, blank=True)
    championship_type = models.CharField( max_length=20, choices=CHAMPIONSHIP_TYPES)
    tier = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Championship"
        verbose_name_plural = "Championships"

    def __str__(self):
        return f"{self.name}"
    def champions(self):
        return self.title_set.all().order_by("-year")
    def get_created_at_utc(self):
        return self.created_at.astimezone(timezone.utc).isoformat()

    def get_updated_at_utc(self):
        return self.updated_at.astimezone(timezone.utc).isoformat()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.name.lower().replace(" ", "-")
        super().save(*args, **kwargs)
