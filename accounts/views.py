from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.auth import  authenticate , login
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            user = authenticate(request , 
                                username=data['username' ], 
                                password=data['password']
                                )
            
            if user is not None :
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Successfully logged in !")
                else : 
                    return HttpResponse("Failed to login !")
                
            else : 
                return HttpResponse("Failed to login or password !")
    else : 
        form = LoginForm()
       
                           
    return render(request,"registration/login.html",{"form" : form})
