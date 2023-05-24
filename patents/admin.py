from django.contrib import admin

from .models import Patent, PatentsDetail


# Register your models here.

class PatentDetailInline(admin.TabularInline):
    model = PatentsDetail
    extra = 1


class PatentAdmin(admin.ModelAdmin):
    inlines = [PatentDetailInline]
    list_display = ('patent_name', 'date', 'project')


admin.site.register(Patent, PatentAdmin)
