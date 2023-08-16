from django import forms
from account.models import User


# Create the form class.
class UserForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('email','password')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError('Passwords not match.')
        return password2
class Userlogin(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
