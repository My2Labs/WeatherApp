import logging
from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from requests import request

class GreetingForm(forms.Form):
    myname = forms.CharField(label='Name')

# def set_session():
#     request.session['myname'] = 'setname'
#     setname = request.session.get('myname', '')
#     return render(request, 'enter.html', {'setname': setname})

