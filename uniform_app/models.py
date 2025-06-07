from django.db import models
from uuid import uuid4
from club_app.models import Club

# Create your models here.
class Uniform(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='uniforms')
    name = models.CharField(max_length=255)
    home_image = models.ImageField(upload_to="clubs/uniforms/home/", null=True, blank=True)
    away_image = models.ImageField(upload_to="clubs/uniforms/away/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Uniform"
        verbose_name_plural = "Uniforms"

    def __str__(self):
        return f"{self.club.name} - {self.name}"