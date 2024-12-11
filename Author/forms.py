from django import forms

from Author.models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'passcode', 'pets_number')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Enter your first name...',
                'maxlength': 40,
                'required': True,
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Enter your last name...',
                'maxlength': 50,
                'required': True,
            }),
            'passcode': forms.PasswordInput(attrs={
                'placeholder': 'Enter 6 digits...',
                'maxlength': 6,
                'required': True,
            }),
            'pets_number': forms.NumberInput(attrs={
                'placeholder': 'Enter the number of your pets...',
                'min': '0',
                'required': True,
            }),
        }
        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'passcode': 'Passcode:',
            'pets_number': 'Pets Number:',
        }
        help_texts = {
            'passcode': 'Your passcode must be a combination of 6 digits'
        }


class EditAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'pets_number', 'info', 'image_url')
        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'pets_number': 'Pets Number:',
            'info': 'Info:',
            'image_url': 'Profile Image URL:',
        }
