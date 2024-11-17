from django.contrib import admin
from .models import Participant
class ParticipantAdmin(admin.ModelAdmin):
    

admin.site.register(Participant)
