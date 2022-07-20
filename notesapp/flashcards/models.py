from django.db import models
from django.conf import settings

from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from versatileimagefield.fields import VersatileImageField, PPOIField

from notes.models import Tag

class Cardset(models.Model):
    set_name = models.TextField(max_length=150, unique=True)
    # Add ording to Cardset model for Pagination so the ordering
    # doesnt change between pages
    class Meta:
        ordering = ["set_name"]

    def __str__(self):
        return self.set_name

class Card(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,  db_index=True)
    modified_at = models.DateTimeField(auto_now=True,  db_index=True)

    question = models.TextField()
    answer = models.TextField()

    cardsets = models.ManyToManyField(Cardset, related_name="cards")

    tags = models.ManyToManyField(Tag, related_name="flashcards")

    card_image = VersatileImageField(
        upload_to="card_images",
        ppoi_field="ppoi",
        null=True,
        blank=True
    )
    # https://django-versatileimagefield.readthedocs.io/en/latest/model_integration.html#model-integration

    ppoi = PPOIField(null=True, blank=True)
    # https://django-versatileimagefield.readthedocs.io/en/latest/specifying_ppoi.html#the-ppoifield


    def __str__(self):
        return self.title