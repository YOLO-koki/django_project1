from django.contrib import admin
from .models import Nikki

# Register your models here.
# 作成したテーブルを管理画面に表示できる様にする
admin.site.register(Nikki)