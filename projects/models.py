from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=200, null=True, default=None)
    date = models.DateField()
    brief_description = models.TextField(blank=True, null=True, default="No Brief Description for this project")
    detail_description = models.TextField(blank=True, null=True, default="No Detail Description for this project")
    project_picture = models.ImageField(upload_to='static/projects/', default='static/projects/default.png')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.project_name


class ProjectsDetail(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    people = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
