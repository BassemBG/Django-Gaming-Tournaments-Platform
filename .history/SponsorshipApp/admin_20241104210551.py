from django.contrib import admin
from .models import sponsorship

@admin.register(sponsorship)
class sponsorshipAdmin(admin.ModelAdmin):
    
