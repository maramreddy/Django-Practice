from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Amount(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    amount = models.IntegerField()
    interest = models.IntegerField()
    startdate = models.DateField()

    def __str__(self):
        return str(self.person) + str(self.amount)

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_link = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='prof_pics',blank=True)
    def __str__(self):
        return self.user.username