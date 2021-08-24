from django.shortcuts import render,HttpResponseRedirect

# Create your views here.

def success(request):
    return render(request,'userapp/success.html')