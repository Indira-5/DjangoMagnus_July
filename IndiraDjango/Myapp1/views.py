from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee, Dept
from .forms import UserForm


# Create your views here.

def home(request):
    data = {"name":"First WebPage"}
    return render(request,'Myapp1/Home.html',context=data)

def help(request):
    return HttpResponse("<h1>This is the Help Page</h1>")

def contact(request):
    return HttpResponse("<h1>This is a Contact page</h1>")

def emp(request):
    emp_data = Employee.objects.all()
    data = {"employee" : emp_data}
    return render(request,'MyApp1/Emp.html',context=data)

def dept(request):
    dept_data = Dept.objects.all()
    appdata = {"Department": dept_data}
    return render(request,'MyApp1/Dept.html',context=appdata)


def form_page(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['user'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['password'])
    return render(request,'MyApp1/UserForm.html',{'form':form})
