from django.contrib import admin
from .models import Supplier, Equipment

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('agency_name', 'f_name', 'l_name', 'phone_num', 'address', 'email', 'sup_type', 'created_date', 'is_active')
    search_fields = ('agency_name', 'f_name', 'l_name', 'email')
    list_filter = ('sup_type', 'is_active')
    ordering = ('agency_name',)

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'brand', 'stock_quantity', 'condition', 'description', 'supplier', 'updated_at', 'is_available')
    search_fields = ('name', 'brand', 'type')
    list_filter = ('condition', 'supplier')
    ordering = ('name',)
    readonly_fields = ('updated_at',)

    # Pour afficher si l'équipement est disponible directement dans la liste
    def is_available(self, obj):
        return obj.is_available()
    is_available.boolean = True  # Affiche un icône booléen dans l'interface

