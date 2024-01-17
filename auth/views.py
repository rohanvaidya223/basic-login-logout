from django.shortcuts import redirect, render
from .form import Registration
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.

def register(request):
    
    
        
    if request.method == 'POST':
        user_form = Registration(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('login')        
    else:
        user_form = Registration()
        return render(request,'registration.html',{'user_form':user_form})
        
def welcome(request):
    return render(request,'welcome.html')


    
