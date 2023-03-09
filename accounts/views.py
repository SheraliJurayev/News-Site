from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import  authenticate , login
from django.contrib.auth.forms import UserCreationForm 
from .forms import LoginForm , UserRegistrationForm 
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Profile
from .forms import UserEditForm , ProfileEditForm

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



def dashboard_view(request):
    user = request.user
    context = {
        'user' : user
    }

    return render (request , 'pages/user_profile.html', context)

def user_register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data["password"]
                )
            new_user.save()

            Profile.objects.create(user = new_user )

            context = {
                "new_user": new_user
            }

        return render(request, 'account/register_done.html', context)
    else:
        user_form = UserRegistrationForm(request.POST)
        context = {
                "user_form": user_form
            }
        return render(request, 'account/register.html' , context)        

class SignUpView(CreateView):
    form_class = UserCreationForm
    succsess_url = reverse_lazy('login')
    template_name = 'account/register.html'

def edit_user(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user , data= request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile , 
                                       data=request.POST , 
                                       files=request.FILES) 
        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile_form.save()

    else:
        user_form =UserEditForm(instance=request.user)
        profile_form =ProfileEditForm(instance=request.profile)

    return render(request, 'account/profile_edit.html', {'user_form': user_form, 'profile_form': profile_form})    