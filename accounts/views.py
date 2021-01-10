from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        #GET all the form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #Password match check
        if password == password2:
            #Check the username is already taken or not
            if User.objects.filter(username=username).exists():
                messages.error(request,'Your given username is already taken !')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email is already used !')
                    return redirect('register')
                else:
                    #All data OK. create the user
                    user = User.objects.create_user(username=username, email=email,password=password, first_name=first_name,last_name=last_name)
                    
                    #OPTION 1: Automatic login user after registration
                    # auth.login(request,user)
                    # messages.success(request,"You are logged in !")
                    # return redirect('index')

                    #OPTION 2: Do not login automattically
                    user.save()
                    messages.success(request,"Registered successfully...")
                    return redirect('login')
        else:
            messages.error(request,'Passwords do not match !')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
