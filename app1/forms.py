from django import forms
from .models import Nikki

# 自作のモデルフォーム
class NikkiForm(forms.ModelForm):
    class Meta:
        model = Nikki
        fields = ('title', 'detail', 'date')
        widgets = {
            'detail': forms.Textarea(attrs={'rows':50, 'cols':150}),
        }