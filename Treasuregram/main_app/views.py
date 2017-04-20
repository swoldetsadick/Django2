# -*- coding: utf-8 -*-
""" This module specifies views. """
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Treasure
from .forms import TreasureForm


def index(request):
    """
    This function orients localhost:port/ type url request
    :param request: A request
    :return: a render element
    """
    treasures = Treasure.objects.all()
    form = TreasureForm()
    return render(request, 'index.html', {'treasures': treasures, 'form': form})


def detail(request, treasure_id):
    """
    This function orients localhost:port/number type url request.
    :param request: A request
    :param treasure_id: a string as treasure ID
    :return: a render element
    """
    treasure = Treasure.objects.get(id=treasure_id)
    return render(request, 'detail.html', {'treasure': treasure})


def post_treasure(request):
    """
    This function add things to forms.
    :param request: A POST request
    :return: A redirects to home page
    """
    form = TreasureForm(request.POST)
    """
    if form.is_valid():
        treasure = Treasure(name=form.cleaned_data['name'], value=form.cleaned_data['value'],
                            material=form.cleaned_data['material'], location=form.cleaned_data['location'],
                            img_url=form.cleaned_data['img_url'])
        treasure.save()
    """
    if form.is_valid():
        form.save(commit=True)
    return HttpResponseRedirect('/')
