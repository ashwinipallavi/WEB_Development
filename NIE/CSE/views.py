from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def products(request):
    name = 'raju'
    department = 'CSE'
    college_name = 'NIE'
    roll_number = 60145
    context = {'name': name, 'c_name': college_name, 'd_name': department, 'r_number':roll_number}
    return render(request,'products.html',  context)

def service(request):
    return render(request,'service.html')

def contacts(request):
    return render(request,'contacts.html')

def studentList(request):
    return render(request,'studentList.html')


def basic(request):
    return render(request,'basic.html')


 #FBV - List view
from CSE.models import Student
def studentList(request):
    students = Student.objects.all()
    context ={'students':students}
    return render(request, 'studentList.html', context)

#FBV 
from CSE.models import Student
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

class StuList(ListView):
    model = Student
    template_name = 'CBV/list.html'


class Forms(CreateView):
    model = Student
    fields = "__all__"
    template_name = 'CBV/forms.html'
    success_url = '/'


class StudentDetail(DetailView):
    model = Student
    template_name = 'CBV/detail.html'

class StudentUpdate(UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'CBV/update.html'
    success_url = '/'

class StudentDelete(DeleteView):
    model = Student
    template_name = 'CBV/delete.html'
    success_url = '/'
