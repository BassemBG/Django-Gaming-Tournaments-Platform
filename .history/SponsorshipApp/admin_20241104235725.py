from django.contrib import admin
from .models import sponsorship

@admin.register(sponsorship)
class sponsorshipAdmin(admin.ModelAdmin):
    actions = ['mark_as_corporate', 'mark_as_small_business', 'mark_as_governmental', 'mark_as_no_defined']

    def mark_as_pending(self, request, queryset):
        queryset.update(status="pending")
        self.message_user(request, ("Selected sponsors marked as Corporate."))

    def mark_as_rejected(self, request, queryset):
        queryset.update(type="rejected")
        self.message_user(request,("Selected sponsors marked as Small Business."))

    def mark_as_approved(self, request, queryset):
        queryset.update(type="governmental")
        self.message_user(request, ("Selected sponsors marked as Governmental."))
        
    def mark_as_terminated(self, request, queryset):
        queryset.update(type="governmental")
        self.message_user(request, ("Selected sponsors marked as Governmental."))
