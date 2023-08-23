from django import forms

class GreetingForm(forms.Form):
    name = forms.CharField()
    address = forms.TextInput()