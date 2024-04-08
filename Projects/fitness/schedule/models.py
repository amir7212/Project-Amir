from django.contrib.auth.models import User
from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

class Gym(models.Model):
    name = models.CharField(max_length=255)

class Trainer(models.Model):
    full_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    gyms = models.ManyToManyField(Gym)

    def __str__(self):
        return self.full_name

class Schedule(models.Model):
    trainer = models.ForeignKey(User, on_delete=models.CASCADE)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.trainer.full_name} - {self.day} {self.start_time}-{self.end_time}"
    
class Booking(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.client.username} - {self.day} {self.start_time}-{self.end_time}"

        
