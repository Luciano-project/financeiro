from django import forms
from .models import ControleFinanceiro
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm

# It tells django that we want use model Item for the current fields
class ItemForm(forms.ModelForm):
    class Meta:
        model = ControleFinanceiro
        fields = ['descricao','valor','categoria','receita_despesa', 'data_registro']

class Userform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']

class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1','new_password2']
    