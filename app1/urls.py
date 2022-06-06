import imp
from django.urls import path
from .views import NikkiList, NikkiDetail

urlpatterns = [
    path('', NikkiList.as_view(), name='contents'),
    path('detail/<int:pk>', NikkiDetail.as_view(), name='detail'),
]

