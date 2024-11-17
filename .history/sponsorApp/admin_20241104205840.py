from django.contrib import admin

@admin.register(sponsor)
class sponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address', 'website', 'type')
