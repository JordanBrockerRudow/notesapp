from django.urls import path, reverse_lazy
from django.views.generic import TemplateView
from . import views

app_name='flashcards'
urlpatterns = [
    path('', views.FlashCardsIndexView.as_view(), name="flashcards-index"),
    path('cardsets/', views.CardsetIndexView.as_view(), name='cardsets-index'),
]
