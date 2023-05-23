from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Patents(models.Model):
    patent_name = models.CharField(max_length=100, null=True, default=None)
    date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


class PatentsDetail(models.Model):
    patent = models.ForeignKey(Patents, on_delete=models.CASCADE)
    people = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
