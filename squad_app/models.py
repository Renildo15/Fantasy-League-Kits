from django.db import models
from uuid import uuid4
from club_app.models import Club
# Create your models here.
class SquadImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    year = models.PositiveIntegerField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='squads')
    squad_image = models.ImageField(upload_to="clubs/squads/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Squad Image"
        verbose_name_plural = "Squad Images"

    def __str__(self):
        return f"{self.name}"