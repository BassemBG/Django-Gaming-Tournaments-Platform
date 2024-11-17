from django.contrib import admin
from .models import Participant
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['cin', 'username', 'email', 'participant_category']

admin.site.register(Participant,ParticipantAdmin)
