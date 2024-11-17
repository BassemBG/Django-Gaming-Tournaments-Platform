from django.contrib import admin
from .models import Equipment

@admin.register(equipment)
class equipmentAdmin(admin.ModelAdmin):
    pass
