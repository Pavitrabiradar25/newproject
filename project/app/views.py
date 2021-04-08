from django.shortcuts import render,redirect
from app.forms import *
from .models import *
# Create your views here.


def retrieve_data(request):

	if request.method == "POST":
		form = MyForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = MyForm()

	if request.method == "POST":

		img = ImageForm(request.POST)
		if img.is_valid():
			img.save()
	else:
		img = ImageForm()

	emp = Student.objects.all()
	return render(request,'app/display.html',{'form':form,'img':img,'emp':emp})

def create_data(request):
	form=StudentForm()
	my_dict = {'form':form}
	if request.method=='POST':
		form=StudentForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')	

	return render(request=request, template_name='app/create.html',context=my_dict)

def delete_view(request,id):
	student=Student.objects.get(id=id)
	student.delete()
	return redirect('/')	


    
