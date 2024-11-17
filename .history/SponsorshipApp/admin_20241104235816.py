from django.contrib import admin
from .models import sponsorship

@admin.register(sponsorship)
class sponsorshipAdmin(admin.ModelAdmin):
    actions = ['mark_as_corporate', 'mark_as_small_business', 'mark_as_governmental', 'mark_as_no_defined']

    def mark_as_pending(self, request, queryset):
        queryset.update(status="Pending")
        self.message_user(request, ("Selected sponsorship marked as Pending."))

    def mark_as_rejected(self, request, queryset):
        queryset.update(type="Rejected")
        self.message_user(request,("Selected sponsorship marked as Small Business."))

    def mark_as_approved(self, request, queryset):
        queryset.update(type="Approved")
        self.message_user(request, ("Selected sponsorship marked as Governmental."))
        
    def mark_as_terminated(self, request, queryset):
        queryset.update(type="Terminated")
        self.message_user(request, ("Selected sponsors marked as Governmental."))
