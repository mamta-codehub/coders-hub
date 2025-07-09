from django.db import models
from django.contrib.auth.models import User
from myadmin.models import Technology,Subtechnology
from company.models import Add_new_vacancy

# Create your models here.

class Profile_user(models.Model):
	phone_number  = models.BigIntegerField()
	gender        = models.CharField(max_length=30)
	date_of_birth = models.DateField()
	address       = models.TextField()
	user = models.OneToOneField(User,on_delete=models.CASCADE,default="")
	date          = models.DateField(auto_now=True)

	class Meta:
		db_table = 'user'

class Project_upload(models.Model):
	title = models.CharField(max_length=100)
	tech    = models.ForeignKey(Technology,on_delete=models.CASCADE)
	subtech    = models.ForeignKey(Subtechnology,on_delete=models.CASCADE)
	abstract  = models.CharField(max_length=400)
	description = models.TextField()
	database = models.CharField(max_length=100)
	tool = models.CharField(max_length=80)
	document = models.CharField(max_length=150)
	sourcecode=models.CharField(max_length=100)
	date = models.DateField(auto_now=True)
	user  = models.ForeignKey(User,on_delete=models.CASCADE)

	class Meta:
		db_table = 'Project_upload'

class Profile_company(models.Model):
	phone_number = models.BigIntegerField()
	address      = models.TextField()
	about_company= models.TextField()
	date          = models.DateField(auto_now=True)
	user = models.OneToOneField(User,on_delete=models.CASCADE)

	class Meta:
		db_table = 'company'

class Post_query(models.Model):
	title = models.CharField(max_length=100)
	tech    = models.ForeignKey(Technology,on_delete=models.CASCADE)
	subtech    = models.ForeignKey(Subtechnology,on_delete=models.CASCADE)
	description = models.TextField()
	file = models.CharField(max_length=150)
	date = models.DateField(auto_now=True)
	user  = models.ForeignKey(User,on_delete=models.CASCADE,default='')

	class Meta:
		db_table ='post_query'


class Contact(models.Model):
 	name = models.CharField(max_length=100)
 	email = models.CharField(max_length=200)
 	phone_no = models.BigIntegerField()
 	message = models.TextField()
 	date = models.DateField(auto_now=True)

 	class Meta:
 		db_table='contact'

class Feedback(models.Model):
	rate = models.CharField(max_length=30)
	message = models.TextField()
	user  = models.ForeignKey(User,on_delete=models.CASCADE)
	date = models.DateField(auto_now=True)

	class Meta:
		db_table='feedback'

class Answer(models.Model):
	answer = models.TextField()
	date   = models.DateField(auto_now=True)
	user   = models.ForeignKey(User,on_delete=models.CASCADE)
	que    = models.ForeignKey(Post_query,on_delete=models.CASCADE)

	class Meta:
		db_table = 'answer'

class Resume(models.Model):
	File = models.CharField(max_length=100)
	date = models.DateField(auto_now=True)
	user   = models.ForeignKey(User,on_delete=models.CASCADE)
	vacancy = models.ForeignKey(Add_new_vacancy,on_delete=models.CASCADE,default='')

	class Meta:
		db_table = 'resume'
