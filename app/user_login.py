from django.shortcuts import redirect, render

def REGISTER(request):
    print(request.method)
    print(request.POST)
    return render(request, 'registration/register.html')