"""The most basic views"""

from typing import Any, Dict
from django.views.generic import TemplateView
from django.shortcuts import render
from ..models.page import Page

class IndexView(TemplateView):
    template_name = 'core/index.html'

class ExplorationView(TemplateView):
    template_name = 'core/page/exploración.html'