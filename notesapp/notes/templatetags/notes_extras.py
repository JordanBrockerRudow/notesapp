from django.contrib.auth import get_user_model
from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.utils.html import format_html

from notes.models import Post
import logging


register = template.Library()
logger = logging.getLogger(__name__)
user_model = get_user_model()

# Aurhor profile details (Returns First Name or Full Name)
@register.filter
def author_profile(author, current_user):
    if not isinstance(author, user_model):
        return ""
    if author == current_user:
        return format_html("<strong>me</strong>")

    if author.first_name or author.first_name and author.last_name:
        name = f"{author.first_name}"

    else:
        name = f"{author.username}"

    return format_html('{}', name)

# Author Details (Name / Email Link) and Date of Notes
@register.filter
def author_details(author, current_user):
    if not isinstance(author, user_model):
        # return empty string as safe default
        return ""

    if author == current_user:
        return format_html("<strong>me</strong>")

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    if author.email:
        prefix = format_html('<a href="mailto:{}" class="txt-cb">', author.email)
        suffix = format_html("</a>")
    else:
        prefix = ""
        suffix = ""

    return format_html('{}{}{}', prefix, name, suffix)

@register.filter
def user_email(current_user):
    if not isinstance(user_model):
        # return empty string as safe default
        return ''
    if current_user.is_active:
        linktag = format_html('<a class="dropdown-item" href="/api/v1/">{}</a>', current_user.email)
        return format_html('<li>{}</li>', linktag)

# Fetch the five most recent notes
# Exclude current post being viewed
@register.inclusion_tag("notes/notes-list.html")
def recent_posts(post):
    posts = Post.objects.exclude(pk=post.pk)[:5]
    # Log call for 'recent posts' - template fragment caching
    logger.debug("Loaded %d recent posts for post %d", len(posts), post.pk)
    return {"title": "Recent Posts", "posts": posts}


# Simple tag for divs with optional bootstrap class input
@register.simple_tag
def div(cls=''):
    if cls == 'close' or cls == 'end':
        return format_html('</div>')

    return format_html('<div class="{}">', cls)



@register.filter
def replace_at(email):
    return str(email).replace('@', '%40')