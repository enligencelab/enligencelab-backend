from django.contrib import admin
from .models import Project, ProjectsDetail


# Register your models here.


class ProjectDetailInline(admin.TabularInline):
    model = ProjectsDetail
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectDetailInline]
    list_display = ('project_name', 'date')


admin.site.register(Project, ProjectAdmin)
