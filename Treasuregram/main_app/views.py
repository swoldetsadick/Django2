# -*- coding: utf-8 -*-
""" This module specifies views. """
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Treasure
from .forms import TreasureForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


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
    form = TreasureForm(request.POST, request.FILES)
    """
    if form.is_valid():
        treasure = Treasure(name=form.cleaned_data['name'], value=form.cleaned_data['value'],
                            material=form.cleaned_data['material'], location=form.cleaned_data['location'],
                            img_url=form.cleaned_data['img_url'])
        treasure.save()
    """
    if form.is_valid():
        treasure = form.save(commit=False)
        treasure.user = request.user
        treasure.save()
    return HttpResponseRedirect('/')


def profile(request, username):
    """
    This function sets a profile.
    :param request: A request
    :param username: A user name
    :return: A render
    """
    user = User.objects.get(username=username)
    treasures = Treasure.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'treasures': treasures})


def login_view(request):
    """
    This function renders login view.
    :param request: A request
    :return: Render or redirect
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The account has been disabled!")
            else:
                print("The username and password were incorrect.")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    """
    Logout view renderer
    :param request: A request
    :return:
    """
    logout(request)
    return HttpResponseRedirect('/')
