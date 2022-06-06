from dataclasses import fields
from statistics import mode
from django import forms
from .models import Nikki

# 自作のモデルフォーム
class NikkiForm(forms.ModelForm):
    class Meta:
        model = Nikki
        fields = ('title', 'detail', 'date')