from django import forms

class ContactForm(forms.Form):
    username = forms.CharField(label="your name", widget=forms.TextInput(
        attrs= {
            "class": "form-control", "placeholder": "example"
        }
    ))
    email = forms.EmailField(label="your email", widget=forms.EmailInput(
        attrs= {
            "class": "form-control", "placeholder": "example@example.example"
        }
    ))
    message = forms.CharField(label="message", widget=forms.Textarea(
        attrs= {
            "class": "form-control", "placeholder": "message", "rows": 5, "cols": 5
        }
    ))