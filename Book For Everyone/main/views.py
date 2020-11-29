from django.shortcuts import render
from .models import Book
from .forms import BookForm

def index(request):
	if request.GET:
		return show(request,search = request.GET['search'])
	return render(request,'index.html',{})

def show(request,search = ''):
	x = Book.objects.all()
	if request.GET:
		search = request.GET['search']
	if search != '':
		x = [i for i in x if search in i.title]
		return render(request,'show.html',{'o':x})
	return render(request,'show.html',{'o':x})

def bookform(request):
	if request.GET:
		return show(request,search = request.GET['search'])
	if request.POST:
		f = BookForm(request.POST or None,request.FILES)
		if f.is_valid():
			f.save()
			f = BookForm()
			return render(request,'getform.html',{'f':f,'success':'Thanks For Your Contribution'})
	else:
		f = BookForm()
	return render(request,'getform.html',{'f':f,'success':''})

def about(request):
	if request.GET:
		return show(request,search = request.GET['search'])
	return render(request,'about.html',{})

