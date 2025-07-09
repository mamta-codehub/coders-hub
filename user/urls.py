"""codershub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('store_contact', views.store_contact, name='store_contact'),
    path('registration_user/', views.registration_user, name='registration_user'),
    path('user_store', views.user_store, name='user_store'),
    path('company_store', views.company_store, name='company_store'),
    path('about_us/', views.about_us, name='about_us'),
    path('login_user/', views.login_user, name='login_user'),
    path('login_user_check', views.login_user_check, name='login_user_check'),
    path('login_company/', views.login_company, name='login_company'),
    path('login_company_check', views.login_company_check, name='login_company_check'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('registration_company/', views.registration_company, name='registration_company'),
    path('feedback/', views.feedback, name='feedback'),
    path('feedback_store', views.feedback_store, name='feedback_store'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('post_query/', views.post_query, name='post_query'),
    path('post_query_store', views.post_query_store, name='post_query_store'),
    path('getandanswer/', views.getandanswer, name='getandanswer'),
    path('Manageproject/', views.Manageproject, name='Manageproject'),
    path('jobportal/', views.jobportal, name='jobportal'),
    path('project/', views.project, name='project'),
    path('project_download/<int:id>', views.project_download, name='project_download'),
    path('upload_project/', views.upload_project, name='upload_project'),
    path('upload_project_store', views.upload_project_store, name='upload_project_store'),
    path('reset_pass/', views.reset_pass, name='reset_pass'),
    path('all_query/', views.all_query, name='all_query'),
    path('query_moredetails/<int:id>', views.query_moredetails, name='query_moredetails'),
    path('view_allanswer/<int:id>', views.view_allanswer, name='view_allanswer'),
    path('post_answer/<int:id>', views.post_answer, name='post_answer'),
    path('answer_store/<int:id>', views.answer_store, name='answer_store'),
    path('job/', views.job, name='job'),
    path('job_details/<int:id>', views.job_details, name='job_details'),
    path('job_apply/<int:id>', views.job_apply, name='job_apply'),
    path('store_job/<int:id>', views.store_job, name='store_job'),
    path('edit_profile_user/', views.edit_profile_user, name='edit_profile_user'),
    path('update_user/<int:id>', views.update_user, name='update_user'),
]
