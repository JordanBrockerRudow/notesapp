from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View

from flashcards.models import Card, Cardset
from flashcards.forms import CardForm

import logging

# Logging
logger = logging.getLogger(__name__)


# Index page for flashcards endpoint
class FlashCardsIndexView(LoginRequiredMixin, View):
    def get(self, request):
        cardset_count = Cardset.objects.all().count()

        cards = Card.objects.all()
        logger.debug("Got %d flashcards", len(cards))
        context = {'cardset_count':cardset_count, 'cards':cards}
        return render(request, template_name='flashcards/flashcards-index.html', context=context)

# Index page for cardsets
class CardsetIndexView(LoginRequiredMixin, View):
    def get(self, request):
        cardsets = Cardset.objects.all()
        logger.debug("Got %d flashcards", len(cardsets))
        context = {'cardsets':cardsets}
        return render(request, template_name='flashcards/cardsets-list.html', context=context)
