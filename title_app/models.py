from django.db import models
from uuid import uuid4

from club_app.models import Club
from championship_app.models import Championship

# Create your models here.
class Title(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='titles')
    championship = models.ForeignKey(Championship, on_delete=models.CASCADE, related_name='titles')
    year = models.PositiveIntegerField()
    coach = models.CharField(max_length=255, blank=True, null=True)
    captain = models.CharField(max_length=255, blank=True, null=True)
    runner_up = models.ForeignKey(
        Club, 
        on_delete=models.SET_NULL, 
        related_name='runner_ups', 
        blank=True, 
        null=True
    )
    top_scorer = models.CharField(max_length=255, blank=True, null=True)
    top_scorer_goals = models.PositiveIntegerField(blank=True, null=True)
    top_assist = models.CharField(max_length=255, blank=True, null=True)
    top_assist_goals = models.PositiveIntegerField(blank=True, null=True)
    top_goalkeeper = models.CharField(max_length=255, blank=True, null=True)
    top_goalkeeper_clean_sheets = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('club', 'championship', 'year')
        ordering = ['-year']
        verbose_name = "Title"
        verbose_name_plural = "Titles"

    def __str__(self):
        return f"{self.club.name} - {self.championship.name} ({self.year})"