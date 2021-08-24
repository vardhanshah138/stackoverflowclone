from django.shortcuts import redirect, render,HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages #import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth.decorators import login_required #to not use any functionalities without login.

# Create your views here.
username = "admin"
def success(request):
	print(request.user)
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


def validate_login(request):
    if not request.user.is_authenticated:
        return login_request(request)


def add_question(request):
	validate_login(request)
	if request.method == "POST":
		p1 = QuestionForm(request.POST)
		if p1.is_valid():
			temp1 = p1.cleaned_data
			Question.objects.create(author=request.user,title = temp1["title"],body = temp1["body"],status = temp1["status"])
			p1 = QuestionForm()
			messages.success(request, "Question added successfully." )
	else:
		p1 = QuestionForm()
	return render(request, "userapp/add_question.html", {"form": p1})



def view_question(request):
	validate_login(request)
	print(request.user.id)
	questions = Question.objects.all().filter(author=request.user)
	print(questions)
	return render(request,"userapp/view_question.html",{"ques" : questions})


def delete_question(request,id):
	validate_login(request)
	if request.method == "POST":
		p=Question.objects.get(pk=id)
		p.delete()
		messages.error(request,"Deleted Successfully")
		return view_question(request)

def update_question(request, id):
    validate_login(request)
    if request.method == "POST":
        p = Question.objects.get(pk=id)
        form_obj = QuestionForm(request.POST, instance=p)
        if form_obj.is_valid():
            messages.success(request, "Updation successful." )
            form_obj.save()
    else:
        p = Question.objects.get(pk=id)
        form_obj = QuestionForm(instance=p)
    return render(request, "userapp/update_question.html", {"form": form_obj})

