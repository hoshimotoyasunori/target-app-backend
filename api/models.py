from django.db import models

# Create your models here.

class Large(models.Model):
    large = models.CharField(max_length=50,blank=True, verbose_name='目的')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id) + " - " + self.large

class Middle(models.Model):
    middle = models.CharField(max_length=50,blank=True, verbose_name='目標')
    target_large = models.ForeignKey(Large, verbose_name='対象の目的', on_delete=models.CASCADE, related_name='related_middle')  #ここ
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id) + " - " + self.middle

class Task(models.Model):
    task = models.CharField(max_length=50,blank=True, verbose_name='タスク')
    target_middle = models.ForeignKey(Middle, verbose_name='対象の目標', on_delete=models.CASCADE, related_name='related_task')  #ここ
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id) + " - " + self.task