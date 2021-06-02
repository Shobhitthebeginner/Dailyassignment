from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def indexView(request):
    return render(request,'index.html')
@login_required
def dashboardViews(request):
    return render(request,"dashboard.html")


def registerViews(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm()
    return render(request,"register.html",{'form':form})
def logoutViews(request):
    return render(request,"logout.html")