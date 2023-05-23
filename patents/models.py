from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Patent(models.Model):
    patent_name = models.CharField(max_length=100, null=True, default=None)
    date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.patent_name


class PatentsDetail(models.Model):
    patent = models.ForeignKey(Patent, on_delete=models.CASCADE)
    people = models.ForeignKey(User, on_delete=models.CASCADE)
    patent_photo = models.ImageField(upload_to='patent-photos/', default='patent-photos/default.png')
    is_active = models.BooleanField(default=True)
