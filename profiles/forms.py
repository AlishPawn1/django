from django import forms

class ProfileCustomForm(forms.Form):
    first_name = forms.CharField(
        label = "first name",
        widget = forms.TextInput(
            attrs={
                "class": "form-control mb-3",
            }
        ),
    )
    last_name = forms.CharField(
        label = "last name",
        widget = forms.TextInput(
            attrs={
                "class": "form-control mb-3",
            }
        ),
    )
    email = forms.EmailField(
        label= 'Your Email',  
        required=True, 
        widget=forms.EmailInput(
            attrs={"class":"form-control mb-3"}
        )
    )
    bio = forms.CharField(
        label = "user description",
        widget = forms.Textarea(
            attrs = {
                "class": "form-control mb-3",
            }
        ),
    )
    profile_image = forms.ImageField(required = True)
    
    
from profiles.models import UserProfile

class ProfilesModelForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"
        
    # def clean_title(self):
    #     title = self.cleaned_data.get('title')
    #     if len(title) < 5:
    #         raise forms.ValidationError("Title field must have at least 5 letters.")
    #     return title