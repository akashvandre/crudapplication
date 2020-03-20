from django.shortcuts import render, redirect
from .models import Addmition

# Create your views here.

def index(request):
	adlist = Addmition.objects.all()
	return render(request, "crud/index.html", {'adlist':adlist})

def create(request):
	return render(request, "crud/create.html")

def stored(request):
	if request.method == 'POST':
		name = request.POST.get('name', '')
		email = request.POST.get('email', '')
		password = request.POST.get('password', '')
		phone = request.POST.get('phone', '')
		wclass = request.POST.get('wclass', '')
		stream = request.POST.get('stream', '')
		fees = request.POST.get('fees', '')
		pending_fees = request.POST.get('pending_fees', '')
		dob = request.POST.get('dob', '')
		adlist = Addmition(name=name, email=email, password=password, phone=phone, wclass=wclass, stream=stream, fees=fees, pending_fees=pending_fees, dob=dob)
		adlist.save()		
	return render(request, "crud/stored.html")

def delete(request, id):
	adlist = Addmition.objects.filter(am_id=id)
	adlist.delete()
	return redirect('/index')

def edit(request, id):
	adlist = Addmition.objects.get(am_id=id)

	return render(request, "crud/edit.html", {'adlist':adlist})

def update(request, id):
	adlist = Addmition.objects.get(am_id=id)
	name = request.POST.get('name', '')
	email = request.POST.get('email', '')
	password = request.POST.get('password', '')
	phone = request.POST.get('phone', '')
	wclass = request.POST.get('wclass', '')
	stream = request.POST.get('stream', '')
	fees = request.POST.get('fees', '')
	pending_fees = request.POST.get('pending_fees', '')
	dob = request.POST.get('dob', '')
	adlist.name = name
	adlist.email = email
	adlist.password = password
	adlist.phone = phone
	adlist.wclass = wclass
	adlist.stream = stream
	adlist.fees = fees
	adlist.pending_fees = pending_fees
	adlist.dob = dob
	adlist.save()
	return redirect('/index')

def about(request):
	return render(request, "crud/about.html")


