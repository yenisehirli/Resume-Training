from django.contrib import admin
from core.models import *

# Register your models here.

@admin.register(GeneralSetting)
class GeneralsettingAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'description', 'parameter', 'update_date', 'created_date']
    search_fields = ['name', 'description', 'parameter']
    list_editable = ['description', 'parameter']

    class Meta:
        model = GeneralSetting
