"""api_automation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from api_test.api.projectList import ProjectList, AddProject, DelProject
from api_test.api.caseList import AddCase, GetCase
from api_test.api import user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('project/project_list', ProjectList.as_view()),
    path('user/login', user.obtain_auth_token),
    path('project/get', ProjectList.as_view()),
    path('project/add', AddProject.as_view()),
    path('project/del', DelProject.as_view()),
    path('case/add', AddCase.as_view()),
    path('case/get', GetCase.as_view()),
    
]

    