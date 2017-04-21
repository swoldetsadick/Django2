# -*- coding: utf-8 -*-
""" This module defines Treasure form """
from django import forms
from .models import Treasure

"""
class TreasureForm(forms.Form):
    "" This is Treasure form class. ""
    name = forms.CharField(label='Name', max_length=100)
    value = forms.DecimalField(label='Value', max_digits=10, decimal_places=2)
    material = forms.CharField(label='Material', max_length=100)
    location = forms.CharField(label='Location', max_length=100)
    img_url = forms.CharField(label='Image URL', max_length=255)
"""


class TreasureForm(forms.ModelForm):
    """ This is Treasure form class using meta class"""
    class Meta:
        """ This is meta class we got from forms"""
        model=Treasure
        exclude=[]
        fields=['name','value','material','location','image'] # 'img_url'


class LoginForm(forms.Form):
    """ This is Treasure form class using meta class"""
    username = forms.CharField(label='User Name', max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())
