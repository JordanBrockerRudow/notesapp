from django.contrib.auth import get_user_model
from django import template
from django.utils.html import format_html

import logging


register = template.Library()
logger = logging.getLogger(__name__)
user_model = get_user_model()

# HTML For Loader Animation
# https://loading.io/css/
@register.simple_tag
def loader():
    return format_html('<div class="lds-default"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>')