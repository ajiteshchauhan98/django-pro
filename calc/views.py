from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
	n=input("input")
	#return HttpResponse("<h1>answer</h1>")
	return render(request,'home.html',{'name':n})
def add(request):
	val1=int(request.POST['num1'])
	val2=int(request.POST['num2'])
	res=val1+val2
	return render(request,'result.html',{'result':res})