from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
@csrf_protect
def login_view(request):
    # Cek apakah user sudah login
    if request.user.is_authenticated:
        messages.info(request, 'Anda sudah login!')
        return redirect('car_list')
        
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login berhasil!')
            return redirect('car_list')
        else:
            messages.error(request, 'Username atau password salah!')
    
    return render(request, 'accounts/login.html')

def is_admin(user):
    return user.is_authenticated and user.is_staff

@csrf_protect
def register_view(request):
    # Cek apakah user adalah admin
    if not (request.user.is_authenticated and request.user.is_staff):
        messages.error(request, 'Hanya admin yang dapat membuat akun baru!')
        return redirect('login')
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            messages.error(request, 'Password tidak cocok!')
            return render(request, 'accounts/register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username sudah digunakan!')
            return render(request, 'accounts/register.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email sudah digunakan!')
            return render(request, 'accounts/register.html')
        
        user = User.objects.create_user(username=username, email=email, password=password1)
        messages.success(request, 'Registrasi berhasil! Silakan login.')
        return redirect('login')
    
    return render(request, 'accounts/register.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout berhasil!')
    return redirect('login')
