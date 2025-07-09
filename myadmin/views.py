from django.shortcuts import render,redirect
from myadmin.models import *
from django.contrib import auth
from django.contrib.auth.models import User
from user.models import Profile_user,Project_upload,Profile_company,Contact,Feedback
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from user.models import *
from .process import html_to_pdf 
from django.template.loader import render_to_string
from datetime import date
from django.conf import settings
from django.views.generic import View

def dashboard(request):
	context = {}
	return render(request,'myadmin/dashboard.html',context)

def common_form(request):
	context = {}
	return render(request,'myadmin/common_form.html',context)

def common_table(request):
	context = {}
	return render(request,'myadmin/common_table.html',context)

def add_technology(request):
	context = {}
	return render(request,'myadmin/add_technology.html',context)

def add_technology_store(request):
	mytechnology = request.POST['tech']
	Technology.objects.create(tech_name=mytechnology)
	return redirect('/myadmin/add_technology')

def all_technology(request):
	result = Technology.objects.all()
	context = {'result':result}
	return render(request,'myadmin/all_technology.html',context)

def all_technology1(request):
	result = Technology.objects.all()
	context = {'result':result}
	return render(request,'myadmin/all_technology1.html',context)

def delete_technology(request,id):
	result = Technology.objects.get(pk=id)
	result.delete()
	return redirect('/myadmin/all_technology1')

def edit_technology(request,id):
	result = Technology.objects.get(pk=id)
	context={'tech':result}
	return render(request,'myadmin/edit_technology.html',context)

def update_technology(request,id):
	data = {
	'tech_name' :request.POST['tech']
	}
	Technology.objects.update_or_create(pk=id,defaults=data)
	return redirect('/myadmin/all_technology1')


def add_subtechnology(request):
	result = Technology.objects.all()
	context = {'tech':result}
	return render(request,'myadmin/add_subtechnology.html',context)

def add_subtechnology_store(request):
	mysubtechnology = request.POST['subtech']
	mytech          = request.POST['techid']
	Subtechnology.objects.create(subtech_name=mysubtechnology,tech_id=mytech)
	return redirect('/myadmin/add_subtechnology')

def all_subtechnology(request):
	result = Subtechnology.objects.all()
	context = {'subtech':result}
	return render(request,'myadmin/all_subtechnology.html',context)

def delete_subtechnology(request,id):
	result = Subtechnology.objects.get(pk=id)
	result.delete()
	return redirect('/myadmin/all_subtechnology')

def edit_subtechnology(request,id):
	result = Subtechnology.objects.get(pk=id)
	result1 = Technology.objects.all()
	context = {'subtech':result,'tech':result1}
	return render(request,'myadmin/edit_subtechnology.html',context)

def update_subtechnology(request,id):
	data ={
	'subtech_name':request.POST['subtech'],
	'tech_id':request.POST['techid']
	}
	Subtechnology.objects.update_or_create(pk=id,defaults=data)
	return redirect('/myadmin/all_subtechnology')

def user(request):
	result = Profile_user.objects.all()
	context = {'result':result}
	return render(request,'myadmin/user.html',context)

def company(request):
	result = Profile_company.objects.all()
	context = {'result':result}
	return render(request,'myadmin/company.html',context)

def project(request):
	result = Project_upload.objects.all()
	context = {'result':result}
	return render(request,'myadmin/project.html',context)

def project_user(request,id):
	result = Project_upload.objects.get(pk=id)
	result1 = Profile_user.objects.get(pk=id)
	context = {'result':result,'result1':result1}
	return render(request,'myadmin/project_user.html',context)

def que_ans(request):
	context = {}
	return render(request,'myadmin/que_ans.html',context)

def feedback(request):
	result=Feedback.objects.all()
	context = {'result':result}
	return render(request,'myadmin/feedback.html',context)

def inquiry(request):
	result = Contact.objects.all()
	context = {'result':result}
	return render(request,'myadmin/inquiry.html',context)

def all_technology(request):
	context = {}
	return render(request,'myadmin/all_technology.html',context)

def login(request):
	context = {}
	return render(request,'myadmin/login.html',context)

def login_check(request):
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(request,username=username,password=password)
		if user is None:
			print("invalid email or password")
			return redirect("/myadmin/login")
		else:
			auth.login(request,user)
			return redirect("/myadmin/dashboard")

def logout(request):
	auth.logout(request)
	return redirect('/myadmin/login')

def sign_up(request):
	context = {}
	return render(request,'myadmin/sign_up.html',context)

def detail_user(request,id):
	result = Profile_user.objects.get(pk=id)
	context = {'result':result}
	return render(request,'myadmin/detail_user.html',context)

def detail_company(request,id):
	result = Profile_company.objects.get(pk=id)
	context = {'result':result}
	return render(request,'myadmin/detail_company.html',context)

def detail_project(request,id):
	result = Project_upload.objects.get(pk=id)
	context = {'result':result}
	return render(request,'myadmin/detail_project.html',context)

def common_form1(request):
	context = {}
	return render(request,'myadmin/common_form1.html',context)

def detail_company1(request):
	context = {}
	return render(request,'myadmin/detail_company1.html',context)

#reports
#user report

def user_report(request):
    if request.method =='POST':
        from_date = request.POST['from_date']
        to_date   = request.POST['to_date']
        result = Profile_user.objects.filter(date__gte=from_date,date__lte=to_date)
        request.session['from_date'] = from_date
        request.session['to_date'] = to_date
        if result.exists():
            context = {'user':result,'f':from_date,'t':to_date} 
        else:
            context = {'user':None} 
    else:
        context = {'user':Profile_user.objects.all()}
    return render(request,'myadmin/user_report.html',context)


class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
        from_date = request.session['from_date']
        to_date   = request.session['to_date']
        data = Profile_user.objects.filter(date__gte=from_date,date__lte=to_date)
        cdate = date.today()
        cdate1 = cdate.strftime('%d/%m/%Y')
        open('templates/temp.html', "w").write(render_to_string('report/result.html', {'data': data,'current_date':cdate1}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')

#2.project report

def project_report(request):
    if request.method =='POST':
        from_date = request.POST['from_date']
        to_date   = request.POST['to_date']
        result = Project_upload.objects.filter(date__gte=from_date,date__lte=to_date)
        request.session['from_date'] = from_date
        request.session['to_date'] = to_date
        if result.exists():
            context = {'user':result,'f':from_date,'t':to_date} 
        else:
            context = {'user':None} 
    else:
        context = {'user':Project_upload.objects.all()}
    return render(request,'myadmin/project_report.html',context)


class project_pdf(View):
     def get(self, request, *args, **kwargs):
        from_date = request.session['from_date']
        to_date   = request.session['to_date']
        data = Project_upload.objects.filter(date__gte=from_date,date__lte=to_date)
        cdate = date.today()
        cdate1 = cdate.strftime('%d/%m/%Y')
        open('templates/temp.html', "w").write(render_to_string('report/project.html', {'data': data,'current_date':cdate1}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')

#3.feedback report

def feedback_report(request):
    if request.method =='POST':
        from_date = request.POST['from_date']
        to_date   = request.POST['to_date']
        result = Feedback.objects.filter(date__gte=from_date,date__lte=to_date)
        request.session['from_date'] = from_date
        request.session['to_date'] = to_date
        if result.exists():
            context = {'user':result,'f':from_date,'t':to_date} 
        else:
            context = {'user':None} 
    else:
        context = {'user':Feedback.objects.all()}
    return render(request,'myadmin/feedback_report.html',context)


class feedback_pdf(View):
     def get(self, request, *args, **kwargs):
        from_date = request.session['from_date']
        to_date   = request.session['to_date']
        data = Feedback.objects.filter(date__gte=from_date,date__lte=to_date)
        cdate = date.today()
        cdate1 = cdate.strftime('%d/%m/%Y')
        open('templates/temp.html', "w").write(render_to_string('report/feedback1.html', {'data': data,'current_date':cdate1}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')

#4.inquiry report

def inquiry_report(request):
    if request.method =='POST':
        from_date = request.POST['from_date']
        to_date   = request.POST['to_date']
        result = Contact.objects.filter(date__gte=from_date,date__lte=to_date)
        request.session['from_date'] = from_date
        request.session['to_date'] = to_date
        if result.exists():
            context = {'user':result,'f':from_date,'t':to_date} 
        else:
            context = {'user':None} 
    else:
        context = {'user':Contact.objects.all()}
    return render(request,'myadmin/inquiry_report.html',context)


class inquiry_pdf(View):
     def get(self, request, *args, **kwargs):
        from_date = request.session['from_date']
        to_date   = request.session['to_date']
        data = Contact.objects.filter(date__gte=from_date,date__lte=to_date)
        cdate = date.today()
        cdate1 = cdate.strftime('%d/%m/%Y')
        open('templates/temp.html', "w").write(render_to_string('report/inquiry1.html', {'data': data,'current_date':cdate1}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')

#5 company report 

def company_report(request):
    if request.method =='POST':
        from_date = request.POST['from_date']
        to_date   = request.POST['to_date']
        result = Profile_company.objects.filter(date__gte=from_date,date__lte=to_date)
        request.session['from_date'] = from_date
        request.session['to_date'] = to_date
        if result.exists():
            context = {'user':result,'f':from_date,'t':to_date} 
        else:
            context = {'user':None} 
    else:
        context = {'user':Profile_company.objects.all()}
    return render(request,'myadmin/company_report.html',context)


class company_pdf(View):
     def get(self, request, *args, **kwargs):
        from_date = request.session['from_date']
        to_date   = request.session['to_date']
        data = Profile_company.objects.filter(date__gte=from_date,date__lte=to_date)
        cdate = date.today()
        cdate1 = cdate.strftime('%d/%m/%Y')
        open('templates/temp.html', "w").write(render_to_string('report/company1.html', {'data': data,'current_date':cdate1}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')