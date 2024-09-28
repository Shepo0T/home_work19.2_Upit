from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm
from django import forms

from Catalog.forms import StyleFormMixin
from users.models import User


class UserRegisterForm( UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

class UserProfileForm(StyleFormMixin, UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'phone', 'avatar', 'country' )


    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields['password'].widget = forms.HiddenInput()

class UserPasswordResetForm(StyleFormMixin, PasswordResetForm):

    class Meta:
        model = User
        fields = ("email",)