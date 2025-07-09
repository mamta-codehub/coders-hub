from django.shortcuts import render,redirect
from company.models import *
from user.models import Profile_company,Resume,Profile_user
from django.contrib import auth
from django.contrib.auth.models import User

def dashboard(request):
    context = {}
    return render(request,'company/dashboard.html',context)

def add_application(request):
    context = {}
    return render(request,'company/add_application.html',context)

def company_store(request):
    Title = request.POST['title']
    Description = request.POST['desc']
    Job_type = request.POST['jobtype']
    location = request.POST['locaton']
    nov = request.POST['nov']
    minimun_salary = request.POST['minsalary']
    Experience = request.POST['experience']
    Date = request.POST['date']
    id = request.user.id
    Add_new_vacancy.objects.create(Title = Title,Description = Description,Job_type = Job_type,Location = location,No_of_vacancy=nov,Min_salary=minimun_salary,Experience=Experience,Date=Date,user_id=id)
    return redirect('/company/add_application/')


def company_delete(request,id):
    result = Add_new_vacancy.objects.get(pk=id)
    result.delete()
    return redirect('/company/all_vacancy')

def company_edit(request,id):
    result = Add_new_vacancy.objects.get(pk=id)
    context = {'result':result}
    return render(request,'company/company_edit.html',context)


def company_update(request,id):
    data = {  
                'Title' :request.POST['title'],
                'Description' :request.POST['Description'],
                'Job_type' :request.POST['jobtype'],
                'Location' :request.POST['location'],
                'No_of_vacancy' :request.POST['nov'],
                'Min_salary' :request.POST['minsalary'],
                'Experience' :request.POST['experience'],
                'Date' :request.POST['Date'],



    }
    Add_new_vacancy.objects.update_or_create(pk=id,defaults=data)
    return redirect('/company/all_vacancy')
    



def all_vacancy(request):
    result = Add_new_vacancy.objects.all()
    context = {'result':result}
    return render(request,'company/all_vacancy.html',context)

def details(request,id):
    result = Add_new_vacancy.objects.get(pk=id)
    context = {'result':result}
    return render(request,'company/details.html',context)


def all_job_application(request):
    result = Resume.objects.all()
    context = {'result':result}
    return render(request,'company/all_job_application.html',context)


def inquiry(request):
    context = {}
    return render(request,'company/inquiry.html',context)


def mydetails(request,id):
    result = Resume.objects.get(pk=id)
    result1 = Profile_user.objects.all()
    context = {'result':result,'result1':result1}
    return render(request,'company/mydetails.html',context)

