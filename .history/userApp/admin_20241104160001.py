from django.contrib import admin
from .models import Participant
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['cin', 'username', 'email', 'participant_category']
    search_fields = ['cin', 'username', 'email', 'participant_category']
    list_filter = ['participant_category']
    ordering = ['username']
    fields = ['cin', 'username', 'email', 'participant_category']
    readonly_fields = ['cin']
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(Participant)
