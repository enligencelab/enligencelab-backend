from django.contrib import admin
from .models import Patents, PatentsDetail

# Register your models here.

admin.site.register(Patents)
admin.site.register(PatentsDetail)
