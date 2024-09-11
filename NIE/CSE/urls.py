"""
URL configuration for NIE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
 from CSE.views import StuList,Forms, StudentDetail, StudentUpdate, StudentDelete


app_name = 'CSE'
urlpatterns = [
 path('index', views.index, name = 'index'),
path('products', views.products, name = 'products'),
path('service', views.service, name = 'service'),
path('contacts', views.contacts, name = 'contacts'),
path('basic', views.basic, name = 'basic'),
path('studentList', views.studentList, name = 'studentList'),


path('', StuList.as_view(), name = 'list'),
path('forms', Forms.as_view(), name = 'forms'),
path('<pk>/detail', StudentDetail.as_view(), name = 'detail'),
path('<pk>/update', StudentUpdate.as_view(), name = 'update'),
path('<pk>/delete', StudentDelete.as_view(), name = 'delete'),
]
