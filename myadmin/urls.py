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
from myadmin import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('common_form/', views.common_form, name='common_form'),
    path('common_table/', views.common_table, name='common_table'),
    path('add_technology/', views.add_technology, name='add_technology'),
    path('add_technology_store', views.add_technology_store, name='add_technology_store'),
    path('all_technology/', views.all_technology, name='all_technology'),
    path('all_technology1/', views.all_technology1, name='all_technology1'),
    path('delete_technology/<int:id>', views.delete_technology, name='delete_technology'),
    path('edit_technology/<int:id>', views.edit_technology, name='edit_technology'),
    path('update_technology/<int:id>', views.update_technology, name='update_technology'),
    path('add_subtechnology/', views.add_subtechnology, name='add_subtechnology'),
    path('add_subtechnology_store', views.add_subtechnology_store, name='add_subtechnology_store'),
    path('delete_subtechnology/<int:id>', views.delete_subtechnology, name='delete_subtechnology'),
    path('edit_subtechnology/<int:id>', views.edit_subtechnology, name='edit_subtechnology'),
    path('update_subtechnology/<int:id>', views.update_subtechnology, name='update_subtechnology'),
    path('user/', views.user, name='user'),
    path('company/', views.company, name='company'),
    path('project/', views.project, name='project'),
    path('project_user/<int:id>', views.project_user, name='project_user'),
    path('que_ans/', views.que_ans, name='que_ans'),
    path('feedback/', views.feedback, name='feedback'),
    path('inquiry/', views.inquiry, name='inquiry'),
    path('all_subtechnology/', views.all_subtechnology, name='all_subtechnology'),
    path('login/', views.login, name='login'),
    path('login_check', views.login_check, name='login_check'),
    path('logout/', views.logout, name='logout'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('detail_user/<int:id>', views.detail_user, name='detail_user'),
    path('detail_company/<int:id>', views.detail_company, name='detail_company'),
    path('detail_project/<int:id>', views.detail_project, name='detail_project'),
    path('common_form1/', views.common_form1, name='common_form1'),
    path('detail_company1/', views.detail_company1, name='detail_company1'),
    
    path('password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    path('user_report', views.user_report, name='user_report'),
    path('pdf/', views.GeneratePdf.as_view()),
    
    path('project_report', views.project_report, name='project_report'),
    path('pdf1/', views.project_pdf.as_view()),

    path('feedback_report', views.feedback_report, name='feedback_report'),
    path('pdf2/', views.feedback_pdf.as_view()),

    path('inquiry_report', views.inquiry_report, name='inquiry_report'),
    path('pdf3/', views.inquiry_pdf.as_view()),

    path('company_report', views.company_report, name='company_report'),
    path('pdf4/', views.company_pdf.as_view()),
]
