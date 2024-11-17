from django.contrib import admin
from .models import participation, Payment
from django.utils.html import format_html


@admin.register(participation)
class participationAdmin(admin.ModelAdmin):
    list_display = ['participant', 'tournament', 'team_name']
    
    # Fields by which the admin can filter the participations
    list_filter = ('participant', 'tournament', 'team_name')
    
    # Fields by which the admin can sort the participations
    ordering = ('participant', 'tournament', 'team_name')
    
    # Number of participations per page
    list_per_page = 25

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
        # Display key fields in the list view
    list_display = ('id', 'participation', 'amount', 'status_colored', 'created_at')

    # Filter by payment status and related tournament
    list_filter = ('status', 'participation__tournament')

    # Search payments by user CIN or tournament name
    search_fields = ('participation__participant__cin', 'participation__tournament__name')

    # Ordering payments by the creation date (newest first)
    ordering = ('-created_at',)

    # Organizing fields in the form view
    fieldsets = (
        (None, {
            'fields': ('participation', 'amount', 'stripe_payment_intent_id', 'status')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)  # Collapsing the timestamp section
        }),
    )

    # Custom bulk actions
    actions = ['mark_as_completed', 'mark_as_failed']

    def mark_as_completed(self, request, queryset):
        queryset.update(status='completed')
        self.message_user(request, "Successfully marked selected payments as completed.")
    mark_as_completed.short_description = "Mark selected payments as completed"

    def mark_as_failed(self, request, queryset):
        queryset.update(status='failed')
        self.message_user(request, "Successfully marked selected payments as failed.")
    mark_as_failed.short_description = "Mark selected payments as failed"

    # Colored labels for the status field
    def status_colored(self, obj):
        color_map = {
            'pending': 'orange',
            'completed': 'green',
            'failed': 'red'
        }
        color = color_map.get(obj.status, 'black')  # Default to black for unknown statuses
        return format_html('<span style="color: {};">{}</span>', color, obj.status)
    status_colored.short_description = 'Status'
