from django.contrib import admin
from .models import Achievement, AchievementsDetail


# Register your models here.


class AchievementDetailInline(admin.TabularInline):
    model = AchievementsDetail
    extra = 1


class AchievementAdmin(admin.ModelAdmin):
    inlines = [AchievementDetailInline]
    list_display = ('achievement_name', 'date', 'project')


admin.site.register(Achievement, AchievementAdmin)
