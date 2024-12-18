from django.shortcuts import render , redirect
from .models import Car
# Create your views here.
def lists(request):
    lists =Car.objects.all()
    context ={
        'list': 'lists',
    }
    return render(request , 'car/list.html',context)
def add(request):
    if request.POST:
        car_name = request.POST['car']
        year_name = request.POST['year']
        Car.objects.update_or_create(brand = car_name , year = year_name) 
        return redirect('lists')
    else:
        return render(request , 'car/add.html')
def delete(request):
    return render(request , 'car/delete.html')