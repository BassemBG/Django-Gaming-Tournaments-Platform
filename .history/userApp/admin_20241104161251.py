from django.contrib import admin
from .models import Participant

@admin.register(Participant)
class YourModelNameAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2', 'field3')
    search_fields = ('field1', 'field2')
    list_filter = ('field1', 'field2')