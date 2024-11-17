from django.contrib import admin
from .models import sponsor

@admin.register(sponsor)
class sponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address', 'website', 'type')
i want an action that 