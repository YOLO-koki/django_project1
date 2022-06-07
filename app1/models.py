from django.db import models
from django.utils import timezone

# Create your models here.
class Nikki(models.Model):
    title = models.CharField(max_length=100, blank=False)
    detail = models.TextField(blank=False)
    date = models.DateTimeField(default=timezone.now())
    
    def __str__(self) -> str:
        return self.title

