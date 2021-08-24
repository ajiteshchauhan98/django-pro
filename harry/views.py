from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from harry.models import Contact
from django.contrib import messages
# Create your views here.

def home(request):
	#return HttpResponse("ye hai")
	#messages.success(request,'test messages')
	return render(request,'new.html')


def about(request):
	#return HttpResponse("about")
	return render(request,'about-harry.html')
def contact(request):
	if request.method == "POST":
		name= request.POST.get('name')
		email= request.POST.get('email')
		phone= request.POST.get('phone')
		desc= request.POST.get('desc')
		password=request.POST.get('pas')
		contact= Contact(name=name, email=email, phone=phone, desc=desc, password=password, date = datetime.today())
		contact.save()
		messages.success(request,'your messages sent !!')
	
	return render(request,'contact-harry.html')

