from django.contrib import admin
from .models import Participant
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'role']

admin.site.register(Participant,ParticipantAdmin)
