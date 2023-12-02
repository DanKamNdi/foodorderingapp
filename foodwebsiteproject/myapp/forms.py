# forms.py
from django import forms


class CartItemForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)
