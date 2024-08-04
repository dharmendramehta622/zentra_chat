from django import forms
from django.contrib.auth.models import User

class OnboardForm(forms.ModelForm):
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password'}), label='New Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}), label='Confirm Password')

    class Meta:
        model = User
        fields = ['username', 'new_password', 'confirm_password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the username field as disabled and not required
        self.fields['username'].disabled = True
        self.fields['username'].required = False
        # Add CSS class to username field
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password and confirm_password and new_password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data
