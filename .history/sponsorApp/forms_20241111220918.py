from django import forms
from .models import Sponsor, Sponsorship, SponsorshipStatus

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



class SponsorshipForm(forms.ModelForm):
    class Meta:
        model = Sponsorship
        fields = ['sponsorship_amount', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

        