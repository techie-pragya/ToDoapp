from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class City(models.Model):
	city_name=models.CharField(max_length=20)

	def __str__(self):
		return self.city_name

class UserProfile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	mobile=models.CharField(max_length=30)
	city=models.ForeignKey(City,on_delete=models.SET_NULL,null=True)
	profpic=models.ImageField(upload_to='profpics')