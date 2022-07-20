from django.contrib.auth import get_user_model
from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.utils.html import format_html

from flashcards.models import Card, Cardset
import logging


register = template.Library()
logger = logging.getLogger(__name__)
user_model = get_user_model()
