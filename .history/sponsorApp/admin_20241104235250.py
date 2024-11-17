from django.contrib import admin
from .models import sponsor

@admin.register(sponsor)
class sponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address', 'website', 'type')

    actions = ['mark_as_corporate', 'mark_as_small_business', 'mark_as_governmental', 'mark_as_no_defined']

    def mark_as_corporate(self, request, queryset):
        queryset.update(type=ty.CORPORATE)
        self.message_user(request, _("Selected sponsors marked as Corporate."))

    def mark_as_small_business(self, request, queryset):
        queryset.update(type=SponsorType.SMALL_BUSINESS)
        self.message_user(request, _("Selected sponsors marked as Small Business."))

    def mark_as_governmental(self, request, queryset):
        queryset.update(type=SponsorType.GOVERNMENTAL)
        self.message_user(request, _("Selected sponsors marked as Governmental."))