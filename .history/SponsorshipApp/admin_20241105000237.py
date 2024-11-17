from django.contrib import admin
from .models import sponsorship

@admin.register(sponsorship)
class SponsorshipAdmin(admin.ModelAdmin):
    
    list_display = ('sponsor', 'tournament', 'amount', 'status')
    actions = ['mark_as_pending', 'mark_as_rejected', 'mark_as_approved', 'mark_as_terminated']

    def mark_as_pending(self, request, queryset):
        queryset.update(status="pending")
        self.message_user(request, ("Selected sponsorship marked as Pending."))

    def mark_as_rejected(self, request, queryset):
        queryset.update(status="rejected")
        self.message_user(request,("Selected sponsorship marked as Rejected."))

    def mark_as_approved(self, request, queryset):
        queryset.update(status="approved")
        self.message_user(request, ("Selected sponsorship marked as Approved."))
        
    def mark_as_terminated(self, request, queryset):
        queryset.update(status="terminated")
        self.message_user(request, ("Selected sponsorship marked as Terminated."))
