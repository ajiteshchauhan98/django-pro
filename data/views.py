from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
	#n=input("input")
	#return HttpResponse("<h1>answer</h1>")
	return render(request,'index.html')

def new(request):
	return HttpResponse("aboyt")

def about(request):
	context={
	"var":"c type insaan",	
	"dus":10,
	
	}
	#n=input("input")
	#return HttpResponse("<h1>answer</h1>")
	return render(request,'about.html',context)