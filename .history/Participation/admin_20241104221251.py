from django.contrib import admin
from .models import participation

@admin.register(participation)
class participationAdmin(admin.ModelAdmin):
    
# Register your models here.
