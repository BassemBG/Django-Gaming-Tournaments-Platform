from django.contrib import admin
from .models import sponsorship

@admin.register(sponsorship)
class sponsorshipAdmin(admin.ModelAdmin):
    actions = ['mark_as_pending', 'mark_as_rejected', 'mark_as_approved', 'mark_as_terminated']

    def mark_as_pending(self, request, queryset):
        queryset.update(status="Pending")
        self.message_user(request, ("Selected sponsorship marked as Pending."))

    def mark_as_rejected(self, request, queryset):
        queryset.update(status="Rejected")
        self.message_user(request,("Selected sponsorship marked as Rejected."))

    def mark_as_approved(self, request, queryset):
        queryset.update(status="Approved")
        self.message_user(request, ("Selected sponsorship marked as Approved."))
        
    def mark_as_terminated(self, request, queryset):
        queryset.update(type="Terminated")
        self.message_user(request, ("Selected sponsorship marked as Terminated."))
