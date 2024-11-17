from django import forms
from .models import sponsor
from SponsorshipApp.models import sponsorship
"""class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = ['identifier', 'email', 'responsible', 'address', 'website', 'type']
        widgets = {
            'type': forms.Select(attrs={
                'class': 'scrollable-dropdown'
            }),
        }
"""


class RegisterSponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsorship
        fields = ['tournament', 'sponsor', 'amount', 'start_date', 'end_date', 'status']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'status': forms.Select(attrs={'class': 'scrollable-dropdown'}),
        }

        