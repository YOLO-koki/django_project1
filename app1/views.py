from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
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
    
# 作成
class NikkiCreate(CreateView):
    model = Nikki
    form_class = NikkiForm
    template_name: str = 'create.html'
    success_url = reverse_lazy('app1:contents')

# 詳細
class NikkiDetail(DetailView):
    model = Nikki
    context_object_name = 'content'
    
# 削除
class NikkiDelete(DeleteView):
    model = Nikki
    context_object_name = 'content'
    success_url = reverse_lazy('app1:contents')