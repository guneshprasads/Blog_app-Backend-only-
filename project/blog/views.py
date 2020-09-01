from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Signup,Newblog
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import pdb
def signup(request):
	if request.method=='POST':
		if Signup.objects.filter(username=request.POST['username']).exists() or Signup.objects.filter(email=request.POST['email']).exists():
			context = {'msg': 'Email or username already exists please enter the new one'}
			return render(request, 'signup.html', context)
		else:
			signup = Signup(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
			signup.save()
			return redirect('login')
	else:
		return render(request,'signup.html')

def login(request):
	if request.method=='POST':
		if Signup.objects.filter(username=request.POST['username'],password=request.POST['password']).exists():
			return redirect('newblog')
		else:
			context = {'msg': 'Invalid username or password'}
			return render(request,'login.html',context)
	else:
		return render(request,'login.html')


def newblog(request):
	if request.method=='POST':
		new=Newblog(blogname=request.POST['blogname'],description=request.POST['description'])
		new.save()
		context = {'msg': 'Blog added succesfully'}
		return render(request,'newblog.html',context)
	else:
		return render(request,'newblog.html')

def logout(request):
	messages.info(request, "Logged out successfully!")
	return redirect('login')

def home(request):
	name=[]
	l=Newblog.objects.values('id')
	q=len(l)
	i=1
	while i<=q:
		n=Newblog.objects.get(id=i)
		context={'id':n.id,'blogname':n.blogname,'description':n.description}
		name.append(context)
		i=i+1
	return render(request,'home.html',{'name': name})



