from django.db import models
from uuid import uuid4

from club_app.models import Club
from championship_app.models import Championship

# Create your models here.
class HistoryChampionship(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='history_championship')
    championship = models.ForeignKey(Championship, on_delete=models.CASCADE, related_name='history_championship')
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
        indexes = [
            models.Index(fields=["championship"]),
            models.Index(fields=["club"]),
            models.Index(fields=["championship", "club"]),
        ]
        unique_together = ('club', 'championship', 'year')
        ordering = ['-year']
        verbose_name = "History Championship"
        verbose_name_plural = "History Championships"

    def __str__(self):
        return f"{self.club.name} - {self.championship.name} ({self.year})"
