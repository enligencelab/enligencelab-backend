from django.db import models
from django.contrib.auth.models import User
from projects.models import Project


# Create your models here.

class Patent(models.Model):
    patent_name = models.CharField(max_length=100, null=True, default=None)
    date = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    patent_photo = models.ImageField(upload_to='static/patent-photos/', default='static/patent-photos/default.jpg')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.patent_name


class PatentsDetail(models.Model):
    patent = models.ForeignKey(Patent, on_delete=models.CASCADE)
    people = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
