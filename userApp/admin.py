from django.contrib import admin
from django.db.models import Count
from django.urls import path
from django.shortcuts import render
from django.utils.html import format_html
from .models import user  # Ensure the correct model is imported


@admin.register(user)
class userAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role', 'dashboard_button')
    search_fields = ('first_name', 'last_name', 'email', 'username')
    list_filter = ('role', 'is_staff')
    ordering = ('-username',)

    # Add a button for viewing the dashboard
    def dashboard_button(self, obj):
        return format_html(
            '<a class="button" href="{}">View Dashboard</a>',
            '/admin/userApp/user/dashboard/'  # Link to the dashboard
        )
    dashboard_button.short_description = "Dashboard"

    def get_urls(self):
        # Default admin URLs
        urls = super().get_urls()
        # Custom URL for the dashboard
        custom_urls = [
            path('dashboard/', self.dashboard_view, name='user_dashboard'),
        ]
        return custom_urls + urls

    def dashboard_view(self, request):
        # Calculate data for the dashboard
        role_counts = user.objects.values('role').annotate(count=Count('role')).order_by('-count')
        staff_count = user.objects.filter(is_staff=True).count()
        Notstaff_count = user.objects.filter(is_staff=False).count()
        print(staff_count)
        total_users = user.objects.count()

        # Prepare data for rendering
        context = {
            'total_users': total_users,
            'staff_count': staff_count,
            'Notstaff_count': Notstaff_count,

            # Data for charts
            'roles': [item['role'] for item in role_counts],
            'role_counts': [item['count'] for item in role_counts],
        }

        # Render the statistics template
        return render(request, 'admin/stat.html', context)
