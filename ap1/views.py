from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
from ap1.models import Car


def car_view(request):
    data = Car.objects.all()
    contax = {
        'car_data': data,
    }
    return render(request, 'car_view.html',contax)

def car_add(request):
    if request.POST:
        company = request.POST.get('company')
        name = request.POST.get('car')
        price = request.POST.get('price')
        Car.objects.create(car_company=company,car_name=name,car_price=price)
        return redirect('/')
    else:
        return render(request, 'car_add.html')

def car_delete(request,id):
    car=Car.objects.get(id=id)
    car.delete()
    return redirect('/')
def car_update(request,id):
    if request.POST:
        company = request.POST.get('company')
        name = request.POST.get('car')
        price = request.POST.get('price')
        Car.objects.filter(id=id).update(car_company=company, car_name=name, car_price=price)
        return redirect('/')
    else:
        data = Car.objects.get(id=id)
        contax = {
            'car_data': data
        }
        return render(request, 'car_update.html', contax)