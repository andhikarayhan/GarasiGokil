from django import forms
from django.forms import ModelForm

from appmain.models import Item


class ItemForm(ModelForm):
    AMOUNT_CHOICES = [(i, str(i)) for i in range(1, 11)]

    amount = forms.ChoiceField(choices=AMOUNT_CHOICES, label="Amount", initial=1, widget=forms.Select)
    class Meta:
        model = Item
        fields = ["brand", "model","amount", "engine_spec"]