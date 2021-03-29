from django.shortcuts import render,redirect
from home.models import Task
from django.contrib import messages
from home.forms import TaskRe



# Create your views here.
def home(request):
    if request.method=='POST':
        fm=TaskRe(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'added successfully')
            fm=TaskRe()
    else:
        fm=TaskRe()

    return render(request,'home/home.html',{'home':'active','form':fm})
def task(request):
    all_tasks=Task.objects.all()
    
    return render(request,'home/task.html',{'task':'active','all_tasks':all_tasks})
def delete(request,id):
    if request.method=='POST':
        di=Task.objects.get(pk=id)
        di.delete()
        messages.success(request,'Your Task Deleted..')
        return  redirect('/tasks')
def update(request,id):
    if request.method=='POST':
        ei=Task.objects.get(pk=id)
        fm=TaskRe(request.POST,instance=ei)
        if fm.is_valid():
            fm.save()
            messages.success(request,'updated successfully!!!')
            return  redirect('/tasks')
        else:
            ei=Task.objects.get(pk=id)
            fm=TaskRe(instance=ei)



    return render(request,'home/update.html',{'form':fm})

