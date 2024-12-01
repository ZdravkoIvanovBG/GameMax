from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from GameMax.app_users.models import Profile

UserModel = get_user_model()


class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


class AppUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['username'].widget.attrs['placeholder'] = 'Email'

        self.fields['password'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'


class AppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email', 'password1', 'password2')

        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control form-control-lg',
                    'placeholder': 'Email'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'

        self.fields['password2'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Your Password'


class ProfileEditForm(forms.ModelForm):
    profile_picture = forms.ImageField(
        widget=forms.FileInput(attrs={'id': 'profile-picture-upload'}),
        label='Click to upload a new photo. (Up to 5mb)'
    )

    class Meta:
        model = Profile
        fields = ('full_name', 'age', 'phone_number', 'profile_picture')

        widgets = {
            'full_name': forms.TextInput(
                attrs={
                    'placeholder': 'Full Name'
                }
            ),
            'age': forms.TextInput(
                attrs={
                    'placeholder': 'Age'
                }
            ),
            'phone_number': forms.TextInput(
                attrs={
                    'placeholder': 'Phone Number',
                }
            ),
        }

    def clean_phone_number(self, *args ,**kwargs):
        phone_number = self.cleaned_data.get('phone_number')

        if len(phone_number) != 10:
            raise ValidationError('Phone Number needs to be exactly 10 characters!')

        return phone_number
