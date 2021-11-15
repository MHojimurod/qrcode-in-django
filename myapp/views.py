from django.db import models
from django.shortcuts import redirect, render
from .models import YourModel
from .forms import YOurMOdelForm
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def home(request):
    model = YourModel()
    form = YOurMOdelForm(request.POST,request.FILES,instance=model)
    if form.is_valid():
        form.save()
        return redirect('home')
    qr_code = YourModel.objects.order_by('-id').filter(user=request.user.id)
    return render(request, 'home.html', {"form":form,"qr_code":qr_code} )

def delete(request,pk):
    model = YourModel.objects.get(pk=pk)
    model.delete()
    return redirect('home')


def loginPAGE(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            print(request.POST)
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect("home")
            else:
                messages.info(request,'invalid login')
                return redirect('login')
        else:
            return render(request,'login.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:    
        if request.method == 'POST':
            print(request.POST)
            req = request.POST
            first_name = req['first_name']
            username = req['username']
            email = req['email']
            password1 = req['password1']
            password2 = req['password2']
            if password1 ==password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request,"User exists")
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,"Email exists")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username,first_name=first_name,email=email,password=password1)
                    user.save()
                    return redirect('login')
            else:
                messages.info(request,"Password is match")
                return redirect('register')
        else:
            return render(request, 'register.html')



def logoutPAGE(request):
    logout(request)
    return redirect('login')