from django.db import models
from uuid import uuid4
# Create your models here.
class Stadium(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Stadium"
        verbose_name_plural = "Stadiums"

    def __str__(self):
        return f"{self.name}"