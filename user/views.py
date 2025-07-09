from django.shortcuts import render,redirect
from user.models import *
from django.contrib import auth
from django.contrib.auth.models import User
from myadmin.models import Technology,Subtechnology
from company.models import Add_new_vacancy
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

def dashboard(request):
	context = {}
	return render(request,'user/dashboard.html',context)

def contact_us(request):
	context = {}
	return render(request,'user/contact_us.html',context)

def store_contact(request):
	name = request.POST['name']
	email = request.POST['email']
	number = request.POST['number']
	message = request.POST['message']
	Contact.objects.create(name=name,email=email,phone_no=number,message=message)
	return redirect("/user/contact_us")

def registration_user(request):
	context = {}
	return render(request,'user/registration_user.html',context)

def user_store(request):
	fname = request.POST['fname']
	lname = request.POST['lname']
	email = request.POST['email']
	number = request.POST['number']
	gender = request.POST['gender']
	dob= request.POST['date']
	address =request.POST['address']
	password = request.POST['pass']
	cpassword = request.POST['cpass']
	username = request.POST['uname']
	if password == cpassword:
		user = User.objects.create_user(first_name=fname,last_name=lname,email=email,password=password,username=username)
		Profile_user.objects.create(phone_number=number,address=address,gender=gender,date_of_birth=dob,user_id=user.id)
		return redirect("/user/dashboard")
	else:
		return redirect('/user/registration_user')

def about_us(request):
	context = {}
	return render(request,'user/about_us.html',context)

def login_user(request):
	context = {}
	return render(request,'user/login_user.html',context)

def login_user_check(request):
	username = request.POST['uname']
	password = request.POST['pass']

	result = auth.authenticate(request,username=username,password=password)

	if result is None:
		return redirect('/user/login_user')
	else:
		auth.login(request,result)
		return redirect('/user/dashboard')

def logout_user(request):
	auth.logout(request)
	return redirect('/user/dashboard')

def login_company(request):
	context = {}
	return render(request,'user/login_company.html',context)

def login_company_check(request):
	username = request.POST['uname']
	password = request.POST['pass']

	result = auth.authenticate(request,username=username,password=password)

	if result is None:
		return redirect('/user/login_company')
	else:
		auth.login(request,result)
		return redirect('/company/dashboard')

def registration_company(request):
	context = {}
	return render(request,'user/registration_company.html',context)

def feedback(request):
	context = {}
	return render(request,'user/feedback.html',context)

def feedback_store(request):
	rate =request.POST['rate']
	message =request.POST['message']
	id = request.user.id
	Feedback.objects.create(rate=rate,message=message,user_id=id)
	return redirect("/user/feedback")

def company_store(request):
	companyname = request.POST['cname']
	ownername = request.POST['oname']
	email = request.POST['email']
	number = request.POST['number']
	address =request.POST['address']
	acompany =request.POST['acomp']
	password = request.POST['pass']
	cpassword = request.POST['cpass']
	username = request.POST['uname']
	if password == cpassword:
		user = User.objects.create_user(first_name=companyname,last_name=ownername,email=email,password=password,username=username)
		Profile_company.objects.create(phone_number=number,address=address,about_company=acompany,user_id=user.id)
		return redirect("/user/dashboard")
	else:
		return redirect('/user/registration_company')


def forgot_password(request):
	context = {}
	return render(request,'user/forgot_password.html',context)

def post_query(request):
	result=Technology.objects.all()
	result1=Subtechnology.objects.all()
	context = {'tech':result,'subtech':result1}
	return render(request,'user/post_query.html',context)

def post_query_store(request):
	title = request.POST['title']
	tech = request.POST['tech']
	subtech = request.POST['subtech']
	description = request.POST['desc']
	file = request.FILES['file']
	id = request.user.id
	mylocation = os.path.join(settings.MEDIA_ROOT,'upload')
	obj = FileSystemStorage(location=mylocation)
	obj.save(file.name,file)
	Post_query.objects.create(title=title,tech_id=tech,subtech_id=subtech,description=description,file=file.name,user_id=id)
	return redirect('/user/post_query')

def getandanswer(request):
	context = {}
	return render(request,'user/getandanswer.html',context)

def Manageproject(request):
	context = {}
	return render(request,'user/Manageproject.html',context)

def jobportal(request):
	context = {}
	return render(request,'user/jobportal.html',context)

def project(request):
	tech_result=Technology.objects.all()
	if request.method == 'POST':
		tech_id = request.POST['tech_name']
		result=Project_upload.objects.filter(tech_id=tech_id)
	else:
		result=Project_upload.objects.all()
	context = {'result':result,'tech_result':tech_result}
	return render(request,'user/project.html',context)

def project_download(request,id):
	result = Project_upload.objects.get(pk=id)
	context = {'result':result}
	return render(request,'user/project_download.html',context)

def upload_project(request):
	result=Technology.objects.all()
	result1=Subtechnology.objects.all()
	context = {'tech':result,'subtech':result1}
	return render(request,'user/upload_project.html',context)

def upload_project_store(request):
	title = request.POST['title']
	abstract = request.POST['abstract']
	desc  = request.POST['desc']
	database = request.POST['data']
	tool = request.POST['tool']
	document = request.FILES['file']
	source = request.FILES['source']
	subtech = request.POST['subtech']
	tech = request.POST['tech']
	id = request.user.id
	mylocation = os.path.join(settings.MEDIA_ROOT,'upload')

	obj = FileSystemStorage(location=mylocation)
	obj.save(document.name,document)
	obj.save(source.name,source)
	Project_upload.objects.create(title=title,abstract=abstract,description=desc,database=database,tool=tool,document=document.name,sourcecode=source,subtech_id=subtech,tech_id=tech,user_id=id)
	return redirect('/user/upload_project')

def reset_pass(request):
	context = {}
	return render(request,'user/reset_pass.html',context)

def all_query(request):
	result = Post_query.objects.all()
	context = {'result':result}
	return render(request,'user/all_query.html',context)

def query_moredetails(request,id):
	result = Post_query.objects.get(pk=id)
	context = {'result':result}
	return render(request,'user/query_moredetails.html',context)

def view_allanswer(request,id):
	result=Answer.objects.filter(que_id=id)
	context = {'result':result}
	return render(request,'user/view_allanswer.html',context)

def post_answer(request,id):
	context = {'que_id':id} 
	return render(request,'user/post_answer.html',context)

def answer_store(request,id):
	answer = request.POST['ans']
	user_id = request.user.id
	Answer.objects.create(answer=answer,user_id=user_id,que_id=id)
	return redirect('/user/all_query')

def job(request):
	result = Add_new_vacancy.objects.all()
	context = {'result':result}
	return render(request,'user/job.html',context)	

def job_details(request,id):
	result = Add_new_vacancy.objects.get(pk=id)
	context = {'result':result}
	return render(request,'user/job_details.html',context)	

def job_apply(request,id):
	context = {'vacancy_id':id}
	return render(request,'user/job_apply.html',context)

def store_job(request,id):
	file = request.FILES['resume']
	user_id = request.user.id
	mylocation = os.path.join(settings.MEDIA_ROOT,'upload')

	obj = FileSystemStorage(location=mylocation)
	obj.save(file.name,file)
	Resume.objects.create(File=file.name,user_id=user_id,vacancy_id=id)
	return redirect('/user/job')

def edit_profile_user(request):
	result = Profile_user.objects.get(user_id=request.user.id)
	context = {'result':result}
	return render(request,'user/edit_profile_user.html',context)

def update_user(request,id):
	data = {
	'first_name':request.POST['first_name'],
	'last_name':request.POST['last_name'],
	'email':request.POST['email'],
	'gender':request.POST['gender'],
	'phone_number':request.POST['phone_number'],
	'address':request.POST['address'],
	'username':request.POST['uname'],
	}
	Profile_user.objects.update_or_create(pk=id,defaults=data)
	return redirect('/user/edit_profile_user')

