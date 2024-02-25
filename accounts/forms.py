from django import forms
from django.contrib.auth.forms import  ReadOnlyPasswordHashField

from accounts.models import User

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(
        widget = forms.PasswordInput(attrs={
                    "class": "form-control mb-2"
                }),
    )
    password2 = forms.CharField(
        label = "Conform Password",
        widget = forms.PasswordInput(attrs={
                    "class": "form-control"
                }),
    )
    username = forms.CharField(
        label= 'Username',
        widget=forms.TextInput(attrs={'class' : 'form-control mb-2'}),
    )
    email = forms.EmailField(
        label= 'Your Email Address',
        widget=forms.TextInput(attrs={'class':'form-control mb-2'})
    )
    class Meta:
        model = User
        fields =[ 'username', 'email','password', 'password2']
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError("passwords must match")
        return password
    def save(self, commit= True):
        user = super().save(commit= False)
        user.set_password(self.cleaned_data.get('password'))
        user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    
    class Meta:
        model = User
        fields = ["username", "email", "password"]

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email address", 
            required=True, 
            widget=forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            )
    )
    password = forms.CharField(label = "Password", 
                required=True,
                widget=forms.PasswordInput(
                    attrs={"class": "form-control"}
                )
            )