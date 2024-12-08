from django import forms

class ChatbotForm(forms.Form):
    user_input = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                'id': 'textInput',  # Match the ID defined in your CSS file
                'placeholder': 'Type your query here...',  # Optional placeholder
            }
        )
    )