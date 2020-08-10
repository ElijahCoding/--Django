from django.shortcuts import render

def register(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    pass

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
