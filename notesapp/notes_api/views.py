from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.base import TemplateView

import logging



class NotesAPIHome(TemplateView):

    template_name = "notes_api/api-index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
