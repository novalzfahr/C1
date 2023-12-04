from django import forms
from .models import Promotion

class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ['menu', 'discount_amount', 'start_time', 'end_time']
