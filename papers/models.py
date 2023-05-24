from django.db import models
from django.contrib.auth.models import User
from projects.models import Project


# Create your models here.

class Paper(models.Model):
    paper_name = models.CharField(max_length=100, null=True, default=None)
    date = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    paper_link = models.CharField(max_length=100, null=True, default=None, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.paper_name


class PapersDetail(models.Model):
    patent = models.ForeignKey(Paper, on_delete=models.CASCADE)
    people = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
