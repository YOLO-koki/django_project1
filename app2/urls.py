from django.urls import path
from app2.views import Index

app_name = 'app2'
urlpatterns = [
    path('', Index.as_view(), name='sign_up'),
]