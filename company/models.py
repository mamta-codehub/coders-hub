from django.db import models
from django.contrib.auth.models import User

class Add_new_vacancy(models.Model):
	Title = models.CharField(max_length=50)
	Description = models.TextField()
	Job_type = models.CharField(max_length=30)
	Location = models.TextField()
	No_of_vacancy = models.CharField(max_length=20)
	Min_salary = models.TextField()
	Experience = models.CharField(max_length=30)
	Date = models.DateField(auto_now=True)
	user  = models.ForeignKey(User,on_delete=models.CASCADE,default='')

	class Meta:
		db_table = 'add_new_vacancy'
