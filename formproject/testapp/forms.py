from django import forms

class registrationForm(forms.Form):
    fname=forms.CharField()
    email=forms.EmailField()