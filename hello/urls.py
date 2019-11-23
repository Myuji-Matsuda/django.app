# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 03:00:19 2019

@author: Owner
"""


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]