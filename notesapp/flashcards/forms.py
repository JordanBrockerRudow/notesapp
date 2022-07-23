from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from flashcards.models import Card, Cardset
class CardSetForm(forms.ModelForm):
  class Meta:
    model = Cardset
    fields = ["set_name"]

  def __init__(self, *args, **kwargs):
    super(CardSetForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.add_input(Submit('submit', 'Submit'))

class CardForm(forms.ModelForm):
  class Meta:
    model = Card
    fields = ["question", "answer", "cardsets", "card_image"]

  def __init__(self, *args, **kwargs):
    super(CardForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.add_input(Submit('submit', 'Submit'))
