from django.contrib import admin
from .models import sponsor

@admin.register(sponsor)
class sponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address', 'website', 'type')
    actions = ['make_active', 'make_inactive']

    def make_active(self, request, queryset):
        queryset.update(status='active')
    make_active.short_description = "Mark selected sponsors as active"

    def make_inactive(self, request, queryset):
        queryset.update(status='inactive')
    make_inactive.short_description = "Mark selected sponsors as inactive"