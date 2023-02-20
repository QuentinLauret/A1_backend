from django import forms
from guitar_shop.models import Guitar

class GuitarForm(forms.ModelForm):  #Class for the form on the main page, able to generate a form for the model Guitar
    class Meta:
        model = Guitar
        fields = "__all__"