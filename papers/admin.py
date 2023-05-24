from django.contrib import admin
from .models import Paper, PapersDetail


# Register your models here.

class PaperDetailInline(admin.TabularInline):
    model = PapersDetail
    extra = 1


class PaperAdmin(admin.ModelAdmin):
    inlines = [PaperDetailInline]
    list_display = ('paper_name', 'date', 'paper_link')


admin.site.register(Paper, PaperAdmin)
