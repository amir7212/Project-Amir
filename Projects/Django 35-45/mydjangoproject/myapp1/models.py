from django.db import models

class Worker(models.Model):
        name = models.CharField(max_length=20, blank=False)
        second_name = models.CharField(max_length=35,blank=False)
        salary = models.IntegerField(default=0)
        
        def __str__(self):
            return f'{self.second_name} {self.name}{self.salary}'

class SalesOrder(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=250)
    
class Progs(models.Model):
        id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=20, blank=False)
        second_name = models.CharField(max_length=35,blank=False)
        age = models.IntegerField(default=0)
        position = models.CharField(max_length=35,blank=False)
        
        def __str__(self):
            return f'{self.id} {self.second_name} {self.name} {self.age} {self.position}'