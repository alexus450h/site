from django.db import models

# Create your models here.
class Food(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField(blank=True)
    photo=models.ImageField(upload_to='photos/%Y/%m/%d')
    time_create=models.DateTimeField(auto_now_add=True)
    time_change=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.title