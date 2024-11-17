from django.contrib import admin
from .models import Equipment

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'description', 'status')
    actions = ['mark_as_available', 'mark_as_unavailable']

    def mark_as_available(self, request, queryset):
        queryset.update(status="available")
        self.message_user(request, ("Selected equipment marked as Available."))

    def mark_as_unavailable(self, request, queryset):
        queryset.update(status="unavailable")
        self.message_user(request,("Selected equipment marked as Unavailable."))
