from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Nikki
from .forms import NikkiForm
from django.db.models import Q

# Create your views here.
# 検索
class NikkiList(ListView):
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        
        if q_word:
            object_list = Nikki.objects.filter(
                Q(title__icontains=q_word) | Q(detail__icontains=q_word)
            )
        else:
            object_list = Nikki.objects.all()
        return object_list
    

class NikkiDetail(DetailView):
    model = Nikki
    context_object_name = 'content'