from django.db import models
from django.contrib.auth.models import User
from projects.models import Project, ProjectsDetail


# Create your models here.

class Achievement(models.Model):
    achievement_name = models.CharField(max_length=200, null=True, default=None)
    date = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.achievement_name


class AchievementsDetail(models.Model):
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    people = models.ForeignKey(User, on_delete=models.CASCADE)
    achievement_photo = models.ImageField(upload_to='static/achievement-photos/',
                                          default='static/achievement-photos/default.jpg')
    is_active = models.BooleanField(default=True)
