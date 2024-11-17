from django.contrib import admin
from .models import Participant

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('id',username', 'email', 'first_name', 'last_name', 'participant_category')
    list_filter = ('participant_category',)
admin.site.register(Participant)
