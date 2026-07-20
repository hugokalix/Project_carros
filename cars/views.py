from django.shortcuts import render, redirect
from django.http import HttpResponse
from cars.models import Car
from cars.forms import CarModelForm


# Create your views here.
def car_view(request):
    cars = Car.objects.all().order_by('model') #aqui o meu usuario vai apontar para meu site e por padrão o banco ja vai filtrar todos os dados
    search = request.GET.get('search')

    if search:
        cars = cars.filter(model__contains=search)

    return render(request, 'cars.html', {'cars': cars})

def new_car_view(request):
    if request.method == 'POST': #aqui estou capturando os dados do meu usuário
        new_car_form = CarModelForm(request.POST, request.FILES) #rebendo dados que o usuário pŕeencheu
        if new_car_form.is_valid(): #verifica que esta valido os dados ou não
            new_car_form.save() #salva no banco de dados
            return redirect('car_list')
    else:
        new_car_form = CarModelForm()
    return render(request, 'new_car.html', {'new_car_form': new_car_form})
