from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from .models import Car

# Create your views here.
@login_required
def car_list(request):
    cars = Car.objects.filter(owner=request.user)
    return render(request, 'cars/car_list.html', {'cars': cars})

@login_required
@csrf_protect
def car_create(request):
    if request.method == 'POST':
        brand = request.POST['brand']
        model = request.POST['model']
        year = request.POST['year']
        color = request.POST['color']
        price = request.POST['price']
        
        car = Car.objects.create(
            brand=brand,
            model=model,
            year=year,
            color=color,
            price=price,
            owner=request.user
        )
        messages.success(request, 'Mobil berhasil ditambahkan!')
        return redirect('car_list')
    
    return render(request, 'cars/car_form.html')

@login_required
def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk, owner=request.user)
    return render(request, 'cars/car_detail.html', {'car': car})

@login_required
@csrf_protect
def car_update(request, pk):
    car = get_object_or_404(Car, pk=pk, owner=request.user)
    
    if request.method == 'POST':
        car.brand = request.POST['brand']
        car.model = request.POST['model']
        car.year = request.POST['year']
        car.color = request.POST['color']
        car.price = request.POST['price']
        car.save()
        
        messages.success(request, 'Mobil berhasil diperbarui!')
        return redirect('car_detail', pk=car.pk)
    
    return render(request, 'cars/car_form.html', {'car': car})

@login_required
@csrf_protect
def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk, owner=request.user)
    
    if request.method == 'POST':
        car.delete()
        messages.success(request, 'Mobil berhasil dihapus!')
        return redirect('car_list')
    
    return render(request, 'cars/car_confirm_delete.html', {'car': car})
