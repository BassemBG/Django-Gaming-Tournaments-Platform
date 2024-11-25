from django import forms
from .models import sponsorship
from TournamentApp.models import tournament

# Form for preselected tournament (hidden field)
class PreselectedSponsorshipForm(forms.ModelForm):
    class Meta:
        model = sponsorship
        fields = ['tournament', 'sponsor', 'amount', 'start_date', 'end_date', 'status']
        widgets = {
            'tournament': forms.HiddenInput(),  # Render tournament as a hidden field
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter amount'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

# Form for selectable tournament (dropdown)
class SelectableSponsorshipForm(forms.ModelForm):
    class Meta:
        model = sponsorship
        fields = ['tournament', 'amount', 'start_date', 'end_date', 'status']
        widgets = {
            'tournament': forms.Select(attrs={'class': 'form-control'}),  # Render tournament as a dropdown
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter amount'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initialize the queryset for the tournament dropdown
        self.fields['tournament'].queryset = tournament.objects.all()
