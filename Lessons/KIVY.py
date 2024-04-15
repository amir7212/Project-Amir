from django.shortcuts import render 
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import Http404
from .models import MyModel 


def about(request):
    return HttpResponse('Пока пайтон')

def home(request):
    return HttpResponse('Привет пайтон')

def greet(request,name):
    return HttpResponse(f'Привет,{name}')

def get_examle(request):
    name=request.GET.get('name','Гость')
    return HttpResponse(f"Привет, {name}!")

def index(request):
    return render(request,"home.html")

def postuser(request):
    name = request.POST.get("name","Undefined")
    age  = request.POST.get("age",1)
    return HttpResponse(f"<h2>Name: {name} Age: {age}</h2>")

def go_home(request):
    return redirect(home)

def my_view(request):
    try:
        obj=MyModel.object.get(pk=1)
    except MyModel.DoesNotExist:
        raise Http404("Обьект не найден")
    return render(request, 'home.html',{'object':obj})



<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">  
    <title>Document</title>
</head>
<body>
    <h2>Form for Users</h2>
    <form method="post" action="postuser/">
        {% csrf_token %}
        <p>Name:<br> <input name="name" /></p>
        <p>Age:<br> <input name="age" type="number" /></p>
        <input type="submit" value="Send" />
    </form>
</body>
</html>


path('about/', views.about),
    path('therd/',views.home),
    path('greet/<str:name>/',views.greet),
    path('get/',views.get_examle),
    path('sss/',views.index),
    path('postuser',views.postuser),
    path('fff/',views.go_home),
    path('404/',views.my_view)
