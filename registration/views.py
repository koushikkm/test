from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import User
from .forms import  UserForm 

# Create your views here.
def index(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        
        if user_form.is_valid():
            user = user_form.save()
            #save hashed password
            user.set_password(user.passwd)
            user.save()
            registered = True
        else:
            #need to handle errors, for the time being user can register again
            pass
    else:    
        user_form = UserForm() 
    
    return render(request, 'registration/index.html', {'user_form':user_form,'registered':registered})
