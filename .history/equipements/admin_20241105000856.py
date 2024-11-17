from django.contrib import admin
from .models import equipment

@admin.register(equipment)
class equipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price', 'category', 'description')
    actions = ['mark_as_available', 'mark_as_unavailable']

    def mark_as_available(self, request, queryset):
        queryset.update(status="available")
        self.message_user(request, ("Selected equipment marked as Available."))

    def mark_as_unavailable(self, request, queryset):
        queryset.update(status="unavailable")
        self.message_user(request,("Selected equipment marked as Unavailable
