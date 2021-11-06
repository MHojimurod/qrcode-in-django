from django.db import models
from django.shortcuts import redirect, render
from .models import YourModel
from .forms import YOurMOdelForm
# Create your views here.

def home(request):
    model = YourModel()
    form = YOurMOdelForm(request.POST,request.FILES,instance=model)
    if form.is_valid():
        form.save()
        return redirect('home')
    qr_code = YourModel.objects.all()
    return render(request, 'home.html', {"form":form,"qr_code":qr_code} )

def delete(request,pk):
    model = YourModel.objects.get(pk=pk)
    model.delete()
    return redirect('home')