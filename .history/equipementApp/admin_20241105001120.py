from django.contrib import admin
from .models import Equipment

@admin.register(Equipment)
class equipmentAdmin(admin.ModelAdmin):
    pass
