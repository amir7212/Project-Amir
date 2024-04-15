from django.shortcuts import render
from myapp1.models import Worker
from django.http import HttpRequest
from django.http import HttpResponse
from myapp1.models import Progs
from django.shortcuts import redirect

def test(requset):
    return render (requset, 'test.html')

def bootstrap_test(request):

    """employees = [
        {'name':'Федор', 'second_name': 'Федоров', 'age': 30, 'position': 'Пайтон разработчик'},
        {'name':'Никита', 'second_name': 'Никитин', 'age': 35, 'position': 'Джанго разработчик'},
        {'name':'Лада', 'second_name': 'Ладова', 'age': 25, 'position': 'Пайтон разработчик'},
        {'name':'Лиза', 'second_name': 'Лизова', 'age': 28, 'position': 'Джава разработчик'},
        {'name':'Амир', 'second_name': 'Амиров', 'age': 30, 'position': 'Пайтон разработчик'}
    ]
    

    if request.method == 'POST':
        print(request.POST)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        second_name = request.POST.get('second_name', '')
        age = request.POST.get('age', 0)
        position = request.POST.get('position', '')
        
        progs_object =Progs.objects.create(name=name, second_name=second_name, age=age, position=position)
        print(progs_object)

    all_progs = Progs.objects.all()
    return render(request, 'bootstrap.html', {'employees': employees, 'all_progs': all_progs})"""

    employees = Progs.objects.all() 

    if request.method == 'POST':
        print(request.POST)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        second_name = request.POST.get('second_name', '')
        age = request.POST.get('age', 0)
        position = request.POST.get('position', '')

        if request.method == 'POST':
            id = request.POST.get('id')
        if id:
            employee = Progs.objects.get(id=id)
            employee.delete()
        
        Progs.objects.create(name=name, second_name=second_name, age=age, position=position)
        redirect ("/")
    return render(request, 'bootstrap.html', {'employees': employees})


def home_view(request):
    context = {
        'title': 'Главная страница',
        'description': 'Это описание главной страницы'
    }
    return render(request,'home.html', context)

def products_view(request):
    products = [
        {'name':'Продукт 1', 'price': 150},
        {'name':'Продукт 2', 'price': 300},
        {'name':'Продукт 3', 'price': 450}
    ]
    return render(request,'products.html',{'products': products})

def index(request):
    return render(request, 'home.html')

def postuser(request):
    name = request.POST.get("name", "Undefined")
    age = request.POST.get("age", 1)
    return HttpResponse(f"<h2>Name: {name} Age: {age}</h2>")

def index_page(request):

    all_workers = Worker.objects.all() 
    

    return render(request,'index.html', context={'data': all_workers})


    #new = Worker(name="Nikita", second_name="Nikitin", salary=200000)
    #new.save()

    #worker_to_change = Worker.objects.get(id=5)
    #worker_to_change.second_name = 'Nikitov'
    #worker_to_change.save()

    #Worker.objects.get(id=5).delete()

    #print(all_workers)
    
    #workers_filtered = Worker.objects.filter(salary=300000)
    #print(workers_filtered)

    for i in all_workers:
        print(f'Фамилия: {i.second_name}, Имя: {i.name}, Зарплата: {i.salary}, ID: {i.id}')

    return render(request, 'index.html')