from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from notes.models import Comment, Post, Tag


class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ["content"]

  def __init__(self, *args, **kwargs):
    super(CommentForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.add_input(Submit('submit', 'Submit'))

class TagForm(forms.ModelForm):
  class Meta:
    model = Tag
    fields = ["value"]

  def __init__(self, *args, **kwargs):
    super(TagForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.add_input(Submit('submit', 'Submit'))


class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ["title", "summary", "content", "tags", "hero_image"]

  def __init__(self, *args, **kwargs):
    super(PostForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.add_input(Submit('submit', 'Submit'))
