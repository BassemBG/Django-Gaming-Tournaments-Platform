from django import forms
from django_recaptcha.fields import ReCaptchaField

class CustomLoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    captcha = ReCaptchaField()

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Extract `request` if provided
        super().__init__(*args, **kwargs)
