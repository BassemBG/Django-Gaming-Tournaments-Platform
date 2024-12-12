from django.contrib import admin
from .models import Supplier, Equipment
from django.urls import path
from django.shortcuts import render
from django.utils.html import format_html
from django.db.models import Count

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('agency_name', 'f_name', 'l_name', 'phone_num', 'address', 'email', 'sup_type', 'created_date', 'is_active')
    search_fields = ('agency_name', 'f_name', 'l_name', 'email')
    list_filter = ('sup_type', 'is_active')
    ordering = ('agency_name',)

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'brand', 'stock_quantity', 'condition', 'description', 'supplier', 'updated_at', 'is_available','dashboard_button')
    search_fields = ('name', 'brand', 'type')
    list_filter = ('condition', 'supplier')
    ordering = ('name',)
    readonly_fields = ('updated_at',)

    # Pour afficher si l'équipement est disponible directement dans la liste
    def is_available(self, obj):
        return obj.is_available()
    is_available.boolean = True  # Affiche un icône booléen dans l'interface
    
    def dashboard_button(self, obj):
        return format_html(
            '<a class="button" href="{}">View Dashboard</a>',
            '/admin/equipmentApp/equipment/dashboard/'  # Link to the dashboard
        )
    dashboard_button.short_description = "Dashboard"

    def get_urls(self):
        # Default admin URLs
        urls = super().get_urls()
        # Custom URL for the dashboard
        custom_urls = [
            path('dashboard/', self.dashboard_view, name='equipment_dashboard'),
        ]
        return custom_urls + urls

    def dashboard_view(self, request):
        # Calculate data for the dashboard
        equipment_count = Equipment.objects.count()

        # Get the count of equipment by condition
        condition_counts = Equipment.objects.values('condition').annotate(count=Count('condition')).order_by('-count')

        # Prepare data for rendering
        context = {
            'equipment_count': equipment_count,

            # Data for pie chart by condition
            'conditions': [item['condition'] for item in condition_counts],
            'condition_counts': [item['count'] for item in condition_counts],
        }

        # Render the statistics template
        return render(request, 'admin/equipment_dashboard.html', context)