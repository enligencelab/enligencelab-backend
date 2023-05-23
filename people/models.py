from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
    is_teacher = models.BooleanField(default=False)
    joined_date = models.DateField()
    graduated_date = models.DateField(null=True, default=None, blank=True)
    is_graduated = models.BooleanField(default=False)
    school = models.CharField(max_length=100, default='上海立信会计金融学院')
    department = models.CharField(max_length=100, default='信息管理学院')
    major = models.CharField(max_length=100, blank=True, null=True, default=None)
    phone_number = models.CharField(max_length=16, blank=True, null=True, default=None)
    school_id_number = models.CharField(max_length=10, null=True, default=None)
    github_account = models.CharField(max_length=100, blank=True, null=True, default=None)

