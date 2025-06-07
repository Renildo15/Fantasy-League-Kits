from uuid import uuid4
from django.db import models
from stadium_app.models import Stadium

# Create your models here.
class Club(models.Model):

    FEDERATIONS_CHOICES = (
        ("FCH", "FCH"),
        ("FCR", "FCR"),
        ("FCM", "FCM"),
    )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=10, blank=True, null=True)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, related_name="clubs")
    emblem = models.ImageField(upload_to="clubs/emblems/", null=True, blank=True)
    federation = models.CharField(choices=FEDERATIONS_CHOICES, default="FCH", max_length=10)
    coach = models.CharField(max_length=255, blank=True, null=True)
    total_titles = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Club"
        verbose_name_plural = "Clubs"

    def titles_championship(self, championship):
        return self.title.filter(championship=championship).count()
    def __str__(self):
        return f"{self.name}"
