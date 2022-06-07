from django.urls import path
from .views import NikkiList, NikkiDetail, NikkiCreate, NikkiDelete

app_name = 'app1'
urlpatterns = [
    path('', NikkiList.as_view(), name='contents'),
    path('detail/<int:pk>', NikkiDetail.as_view(), name='detail'),
    path('delete/<int:pk>', NikkiDelete.as_view(), name='delete'),
    path('create/', NikkiCreate.as_view(), name='create'),
]

