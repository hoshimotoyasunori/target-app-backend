from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Large(models.Model):
    user = models.ForeignKey(User, verbose_name='ユーザー', on_delete=models.CASCADE)
    large = models.CharField(max_length=50,blank=True, verbose_name='目的')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.large

class Middle(models.Model):

    user = models.ForeignKey(User, verbose_name='ユーザー', on_delete=models.CASCADE)
    middle = models.CharField(max_length=50,blank=True, verbose_name='目標')
    target_large = models.ForeignKey(Large, verbose_name='対象の目的', on_delete=models.CASCADE, related_name='related_middle')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.middle

class Task(models.Model):

    user = models.ForeignKey(User, verbose_name='ユーザー', on_delete=models.CASCADE)
    task = models.CharField(max_length=50,blank=True, verbose_name='タスク')
    target_middle = models.ForeignKey(Middle, verbose_name='対象の目標', on_delete=models.CASCADE, related_name='related_task')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.task