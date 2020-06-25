from django.shortcuts import render, redirect
from django.http import HttpResponse


from .models import *
from .forms import *
# Create your views here.

def index(request):
	my_todos= My_todo.objects.all()

	form = My_todoForm()
	# calling forms here

	if request.method == "POST":
		form = My_todoForm(request.POST)
		#calling data which is only taken by POST method.....
		if form.is_valid():
			form.save()
		return redirect('/')

	context = {'my_todos': my_todos,'form': form}
	return render(request, 'my_todo/list.html', context) 


def updateTask(request, pk):

	my_todo = My_todo.objects.get(id=pk)
	form = My_todoForm(instance = my_todo)

	if request.method == 'POST':
		form = My_todoForm(request.POST, instance = my_todo)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form' : form}

	return render(request, 'my_todo/update_task.html', context)


def deleteTask(request, pk):
	item = My_todo.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('/')

	context = {'item': item}
	return render(request, 'my_todo/delete.html', context)