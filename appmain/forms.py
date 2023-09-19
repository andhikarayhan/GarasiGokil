from django.forms import ModelForm

from appmain.models import Item


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["brand", "model","amount", "engine_spec"]