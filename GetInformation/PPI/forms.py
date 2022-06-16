from django import forms

class ProfileForm(forms.Form):
   filename = forms.FileField()
