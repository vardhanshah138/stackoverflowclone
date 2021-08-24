from django.shortcuts import redirect, render,HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages #import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth.decorators import login_required #to not use any functionalities without login.

# Create your views here.

def success(request):
    return render(request,'userapp/success.html')


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			print("You are now logged in as")
			return HttpResponseRedirect('/stackovf/success')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request,"userapp/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request,"You are now logged in as." + username)
				print("You are now logged in as")
				return HttpResponseRedirect('/stackovf/success')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request, "userapp/authlogin.html", {"login_form":form})    

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	print("You have Succesfully Logged out.")
	return HttpResponseRedirect('/stackovf/success')