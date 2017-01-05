# coding:utf-8
from django.shortcuts import render
from django.views.generic import TemplateView

class HomeSiteView(TemplateView):
    template_name = 'core/index.html'
