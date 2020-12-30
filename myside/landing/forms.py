from django import forms
from .models import Subscriber


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber  # На основе какой модели
        exclude = [""]  # поля которые нужно исключить
