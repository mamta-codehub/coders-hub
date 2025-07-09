# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
from django.contrib import admin
from django.urls import path, include
from company import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_application/', views.add_application, name='add_application'),
    path('company_store/', views.company_store, name='company_store'),
    path('company_delete/<int:id>', views.company_delete, name='company_delete'),
    path('company_edit/<int:id>', views.company_edit, name='company_edit'),
    path('company_update/<int:id>', views.company_update, name='company_update'),
    path('all_vacancy/', views.all_vacancy, name='all_vacancy'),
    path('details/<int:id>', views.details, name='details'),
    path('all_job_application/', views.all_job_application, name='all_job_application'),
    path('inquiry/', views.inquiry, name='inquiry'),
    path('mydetails/<int:id>', views.mydetails, name='mydetails'),
    
    

    
]