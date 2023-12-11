from django import forms
from order.models import Promo

class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promo
        fields = ['ID_promo', 'nama_promo', 'deskripsi_promo', 'diskon_promo', 'masa_berlaku']
        widgets = {
            'masa_berlaku': forms.DateInput(attrs={'type': 'date'}),
        }
