from django import forms

class GreetingForm(forms.Form):
    myname = forms.CharField(label='Name')
    myaddress = forms.CharField(label='Address')
    age = forms.IntegerField(label='Age')