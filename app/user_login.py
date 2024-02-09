from django.shortcuts import redirect, render


def REGISTER(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(username,email,password) 
        print(request.method)
        print(request.POST)
    return render(request, 'registration/register.html')
    