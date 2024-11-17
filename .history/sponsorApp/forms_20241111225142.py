from django import forms
from .models import sponsor
from SponsorshipApp.models import sponsorship


class RegisterSponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = ['name', 'email', 'address', 'website', 'type']
        widgets = {
            'type': forms.Select(choices=[('corporate', 'Corporate'), ('small business', 'Small Business'), ('governmental', 'Governmental')]),
        }



class RegisterSponsorForm(forms.ModelForm):
    class Meta:
        model = sponsorship
        fields = ['tournament', 'sponsor', 'amount', 'start_date', 'end_date', 'status']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'status': forms.Select(attrs={'class': 'scrollable-dropdown'}),
        }

        