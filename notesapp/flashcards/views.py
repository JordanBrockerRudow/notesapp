from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.urls import reverse

from flashcards.models import Card, Cardset
from flashcards.forms import CardForm

import logging

# Logging
logger = logging.getLogger(__name__)

# Main Page for Flashcards
def flashcard_index(request):
    # Returns Flashcard Question, Cardset, Datetime
    cards = Card.objects.all()
    # Log quantity of posts
    logger.debug("Got %d flashcards", len(cards))

    return render(request, "flashcards/flashcard.html", {"cards": cards})
