from django import forms
from order.models import Menu

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['ID_menu' ,'nama', 'deskripsi', 'harga']