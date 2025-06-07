from uuid import uuid4
from django.db import models



from pathlib import Path

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
    # squad_image = models.ImageField(upload_to="clubs/squads/", null=True, blank=True) criar uma tabela Squad
    # stadium = models.CharField(max_length=255, blank=True, null=True) criar uma tabela Stadium
    #uniform_home = models.ImageField(upload_to="clubs/uniforms/home/", null=True, blank=True) criar uma tabela Uniform
    #uniform_away = models.ImageField(upload_to="clubs/uniforms/away/", null=True, blank=True)
    #uniform_third = models.ImageField(upload_to="clubs/uniforms/third/", null=True, blank=True)
    emblem = models.ImageField(upload_to="clubs/emblems/", null=True, blank=True)
    federation = models.CharField(choices=FEDERATIONS_CHOICES, default="FCH", max_length=10)
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
