from django.contrib import admin
from .models import equipment

@admin.register(equipment)
class equipmentAdmin(admin.ModelAdmin):
    pass
