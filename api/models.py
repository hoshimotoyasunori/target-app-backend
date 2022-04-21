from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Target(models.Model):

    user = models.ForeignKey(User, verbose_name='ユーザー', on_delete=models.CASCADE,related_name='user_target')
    
    target1_1 = models.CharField(max_length=50,blank=True, verbose_name='1-1')
    target1_2 = models.CharField(max_length=50,blank=True, verbose_name='1-2')
    target1_3 = models.CharField(max_length=50,blank=True, verbose_name='1-3')
    target1_4 = models.CharField(max_length=50,blank=True, verbose_name='1-4')
    target1_5 = models.CharField(max_length=50,blank=True, verbose_name='1-5')
    target1_6 = models.CharField(max_length=50,blank=True, verbose_name='1-6')
    target1_7 = models.CharField(max_length=50,blank=True, verbose_name='1-7')
    target1_8 = models.CharField(max_length=50,blank=True, verbose_name='1-8')
    target1_9 = models.CharField(max_length=50,blank=True, verbose_name='1-9')

    target2_1 = models.CharField(max_length=50,blank=True, verbose_name='2-1')
    target2_2 = models.CharField(max_length=50,blank=True, verbose_name='2-2')
    target2_3 = models.CharField(max_length=50,blank=True, verbose_name='2-3')
    target2_4 = models.CharField(max_length=50,blank=True, verbose_name='2-4')
    target2_5 = models.CharField(max_length=50,blank=True, verbose_name='2-5')
    target2_6 = models.CharField(max_length=50,blank=True, verbose_name='2-6')
    target2_7 = models.CharField(max_length=50,blank=True, verbose_name='2-7')
    target2_8 = models.CharField(max_length=50,blank=True, verbose_name='2-8')
    target2_9 = models.CharField(max_length=50,blank=True, verbose_name='2-9')

    target3_1 = models.CharField(max_length=50,blank=True, verbose_name='3-1')
    target3_2 = models.CharField(max_length=50,blank=True, verbose_name='3-2')
    target3_3 = models.CharField(max_length=50,blank=True, verbose_name='3-3')
    target3_4 = models.CharField(max_length=50,blank=True, verbose_name='3-4')
    target3_5 = models.CharField(max_length=50,blank=True, verbose_name='3-5')
    target3_6 = models.CharField(max_length=50,blank=True, verbose_name='3-6')
    target3_7 = models.CharField(max_length=50,blank=True, verbose_name='3-7')
    target3_8 = models.CharField(max_length=50,blank=True, verbose_name='3-8')
    target3_9 = models.CharField(max_length=50,blank=True, verbose_name='3-9')

    target4_1 = models.CharField(max_length=50,blank=True, verbose_name='4-1')
    target4_2 = models.CharField(max_length=50,blank=True, verbose_name='4-2')
    target4_3 = models.CharField(max_length=50,blank=True, verbose_name='4-3')
    target4_4 = models.CharField(max_length=50,blank=True, verbose_name='4-4')
    target4_5 = models.CharField(max_length=50,blank=True, verbose_name='4-5')
    target4_6 = models.CharField(max_length=50,blank=True, verbose_name='4-6')
    target4_7 = models.CharField(max_length=50,blank=True, verbose_name='4-7')
    target4_8 = models.CharField(max_length=50,blank=True, verbose_name='4-8')
    target4_9 = models.CharField(max_length=50,blank=True, verbose_name='4-9')

    target5_1 = models.CharField(max_length=50,blank=True, verbose_name='5-1')
    target5_2 = models.CharField(max_length=50,blank=True, verbose_name='5-2')
    target5_3 = models.CharField(max_length=50,blank=True, verbose_name='5-3')
    target5_4 = models.CharField(max_length=50,blank=True, verbose_name='5-4')
    target5_5 = models.CharField(max_length=50,blank=True, verbose_name='5-5')
    target5_6 = models.CharField(max_length=50,blank=True, verbose_name='5-6')
    target5_7 = models.CharField(max_length=50,blank=True, verbose_name='5-7')
    target5_8 = models.CharField(max_length=50,blank=True, verbose_name='5-8')
    target5_9 = models.CharField(max_length=50,blank=True, verbose_name='5-9')

    target6_1 = models.CharField(max_length=50,blank=True, verbose_name='6-1')
    target6_2 = models.CharField(max_length=50,blank=True, verbose_name='6-2')
    target6_3 = models.CharField(max_length=50,blank=True, verbose_name='6-3')
    target6_4 = models.CharField(max_length=50,blank=True, verbose_name='6-4')
    target6_5 = models.CharField(max_length=50,blank=True, verbose_name='6-5')
    target6_6 = models.CharField(max_length=50,blank=True, verbose_name='6-6')
    target6_7 = models.CharField(max_length=50,blank=True, verbose_name='6-7')
    target6_8 = models.CharField(max_length=50,blank=True, verbose_name='6-8')
    target6_9 = models.CharField(max_length=50,blank=True, verbose_name='6-9')

    target7_1 = models.CharField(max_length=50,blank=True, verbose_name='7-1')
    target7_2 = models.CharField(max_length=50,blank=True, verbose_name='7-2')
    target7_3 = models.CharField(max_length=50,blank=True, verbose_name='7-3')
    target7_4 = models.CharField(max_length=50,blank=True, verbose_name='7-4')
    target7_5 = models.CharField(max_length=50,blank=True, verbose_name='7-5')
    target7_6 = models.CharField(max_length=50,blank=True, verbose_name='7-6')
    target7_7 = models.CharField(max_length=50,blank=True, verbose_name='7-7')
    target7_8 = models.CharField(max_length=50,blank=True, verbose_name='7-8')
    target7_9 = models.CharField(max_length=50,blank=True, verbose_name='7-9')

    target8_1 = models.CharField(max_length=50,blank=True, verbose_name='8-1')
    target8_2 = models.CharField(max_length=50,blank=True, verbose_name='8-2')
    target8_3 = models.CharField(max_length=50,blank=True, verbose_name='8-3')
    target8_4 = models.CharField(max_length=50,blank=True, verbose_name='8-4')
    target8_5 = models.CharField(max_length=50,blank=True, verbose_name='8-5')
    target8_6 = models.CharField(max_length=50,blank=True, verbose_name='8-6')
    target8_7 = models.CharField(max_length=50,blank=True, verbose_name='8-7')
    target8_8 = models.CharField(max_length=50,blank=True, verbose_name='8-8')
    target8_9 = models.CharField(max_length=50,blank=True, verbose_name='8-9')

    target9_1 = models.CharField(max_length=50,blank=True, verbose_name='9-1')
    target9_2 = models.CharField(max_length=50,blank=True, verbose_name='9-2')
    target9_3 = models.CharField(max_length=50,blank=True, verbose_name='9-3')
    target9_4 = models.CharField(max_length=50,blank=True, verbose_name='9-4')
    target9_5 = models.CharField(max_length=50,blank=True, verbose_name='9-5')
    target9_6 = models.CharField(max_length=50,blank=True, verbose_name='9-6')
    target9_7 = models.CharField(max_length=50,blank=True, verbose_name='9-7')
    target9_8 = models.CharField(max_length=50,blank=True, verbose_name='9-8')
    target9_9 = models.CharField(max_length=50,blank=True, verbose_name='9-9')

    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.target5_5

# class TopLeft(models.Model):
#     user = models.ForeignKey(User, verbose_name='ユーザー', on_delete=models.CASCADE)
#     topleft = models.CharField(max_length=50,blank=True, verbose_name='目標')
#     target_target = models.ForeignKey(Target, verbose_name='対象の目的', on_delete=models.CASCADE, related_name='related_topleft')
#     created_at = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.topleft
