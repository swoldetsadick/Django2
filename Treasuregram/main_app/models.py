# -*- coding: utf-8 -*-
""" This module defines Treasure Model """
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Treasure(models.Model):
    """ Treasure Model"""
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    material = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    # img_url = models.CharField(max_length=255)
    image = models.ImageField(upload_to='treasure_images', default='media/default.png')
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
