from django.db import models

# Create your models here.

class Target(models.Model):
    target1_1 = models.CharField(max_length=50,blank=True)
    target1_2 = models.CharField(max_length=50,blank=True)
    target1_3 = models.CharField(max_length=50,blank=True)
    target1_4 = models.CharField(max_length=50,blank=True)
    target1_5 = models.CharField(max_length=50,blank=True)
    target1_6 = models.CharField(max_length=50,blank=True)
    target1_7 = models.CharField(max_length=50,blank=True)
    target1_8 = models.CharField(max_length=50,blank=True)
    target1_9 = models.CharField(max_length=50,blank=True)
    target2_1 = models.CharField(max_length=50,blank=True)
    target2_2 = models.CharField(max_length=50,blank=True)
    target2_3 = models.CharField(max_length=50,blank=True)
    target2_4 = models.CharField(max_length=50,blank=True)
    target2_5 = models.CharField(max_length=50,blank=True)
    target2_6 = models.CharField(max_length=50,blank=True)
    target2_7 = models.CharField(max_length=50,blank=True)
    target2_8 = models.CharField(max_length=50,blank=True)
    target2_9 = models.CharField(max_length=50,blank=True)
    target3_1 = models.CharField(max_length=50,blank=True)
    target3_2 = models.CharField(max_length=50,blank=True)
    target3_3 = models.CharField(max_length=50,blank=True)
    target3_4 = models.CharField(max_length=50,blank=True)
    target3_5 = models.CharField(max_length=50,blank=True)
    target3_6 = models.CharField(max_length=50,blank=True)
    target3_7 = models.CharField(max_length=50,blank=True)
    target3_8 = models.CharField(max_length=50,blank=True)
    target3_9 = models.CharField(max_length=50,blank=True)
    target4_1 = models.CharField(max_length=50,blank=True)
    target4_2 = models.CharField(max_length=50,blank=True)
    target4_3 = models.CharField(max_length=50,blank=True)
    target4_4 = models.CharField(max_length=50,blank=True)
    target4_5 = models.CharField(max_length=50,blank=True)
    target4_6 = models.CharField(max_length=50,blank=True)
    target4_7 = models.CharField(max_length=50,blank=True)
    target4_8 = models.CharField(max_length=50,blank=True)
    target4_9 = models.CharField(max_length=50,blank=True)
    target5_1 = models.CharField(max_length=50,blank=True)
    target5_2 = models.CharField(max_length=50,blank=True)
    target5_3 = models.CharField(max_length=50,blank=True)
    target5_4 = models.CharField(max_length=50,blank=True)
    target = models.CharField(max_length=50)
    target5_6 = models.CharField(max_length=50,blank=True)
    target5_7 = models.CharField(max_length=50,blank=True)
    target5_8 = models.CharField(max_length=50,blank=True)
    target5_9 = models.CharField(max_length=50,blank=True)
    target6_1 = models.CharField(max_length=50,blank=True)
    target6_2 = models.CharField(max_length=50,blank=True)
    target6_3 = models.CharField(max_length=50,blank=True)
    target6_4 = models.CharField(max_length=50,blank=True)
    target6_5 = models.CharField(max_length=50,blank=True)
    target6_6 = models.CharField(max_length=50,blank=True)
    target6_7 = models.CharField(max_length=50,blank=True)
    target6_8 = models.CharField(max_length=50,blank=True)
    target6_9 = models.CharField(max_length=50,blank=True)
    target7_1 = models.CharField(max_length=50,blank=True)
    target7_2 = models.CharField(max_length=50,blank=True)
    target7_3 = models.CharField(max_length=50,blank=True)
    target7_4 = models.CharField(max_length=50,blank=True)
    target7_5 = models.CharField(max_length=50,blank=True)
    target7_6 = models.CharField(max_length=50,blank=True)
    target7_7 = models.CharField(max_length=50,blank=True)
    target7_8 = models.CharField(max_length=50,blank=True)
    target7_9 = models.CharField(max_length=50,blank=True)
    target8_1 = models.CharField(max_length=50,blank=True)
    target8_2 = models.CharField(max_length=50,blank=True)
    target8_3 = models.CharField(max_length=50,blank=True)
    target8_4 = models.CharField(max_length=50,blank=True)
    target8_5 = models.CharField(max_length=50,blank=True)
    target8_6 = models.CharField(max_length=50,blank=True)
    target8_7 = models.CharField(max_length=50,blank=True)
    target8_8 = models.CharField(max_length=50,blank=True)
    target8_9 = models.CharField(max_length=50,blank=True)
    target9_1 = models.CharField(max_length=50,blank=True)
    target9_2 = models.CharField(max_length=50,blank=True)
    target9_3 = models.CharField(max_length=50,blank=True)
    target9_4 = models.CharField(max_length=50,blank=True)
    target9_5 = models.CharField(max_length=50,blank=True)
    target9_6 = models.CharField(max_length=50,blank=True)
    target9_7 = models.CharField(max_length=50,blank=True)
    target9_8 = models.CharField(max_length=50,blank=True)
    target9_9 = models.CharField(max_length=50,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id) + " - " + self.target
