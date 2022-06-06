from django.db import models

# Create your models here.
class Nikki(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField(blank=False)
    date = models.DateTimeField()
    
    def __str__(self) -> str:
        return self.title

