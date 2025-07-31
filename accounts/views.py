from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate (request, username=username, password = password)

        if user is not None:
            login(request, user)
            return redirect ('dashboard:intro')
        else:
            return render(request,'accounts/login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'accounts/login.html')


@login_required
def welcome_view(request):
    return render(request,'accounts/welcome.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']  # ✅ Remove typo here

        # ✅ Fix typo: should be "objects", not "object"
        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html', {'error': 'Username already taken'})

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('dashboard:intro')

    return render(request, 'accounts/register.html')



#logout
def logout_view(request):
    logout(request)
    return redirect('login')
    