from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .form import  Todoform
from .models import Task
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, DeleteView


# Create your views here.

class tasklistview(ListView):
    model=Task
    template_name='home.html'
    context_object_name='ac'

class detail(DetailView):
    model=Task
    template_name='detail.html'
    context_object_name='deta'

class update(UpdateView):
    model=Task
    template_name='update.html'
    context_object_name='upd'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('d',kwargs={'pk':self.object.id})

class delet(DeleteView):
    model=Task
    template_name='delete.html'
    success_url = reverse_lazy('list')


def funct(request):
    ac=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date', '')
        todo=Task(name=name,priority=priority, date=date)
        todo.save()
    return render(request,'home.html',{'ac':ac})
def delete(request,taskid):
    dele=Task.objects.get(id=taskid)
    if request.method=='POST':
        dele.delete()
        return redirect('/')
    return render(request,'delete.html')
def edit(request,id):
    edit1=Task.objects.get(id=id)
    f1=Todoform(request.POST or None,instance=edit1)
    if f1.is_valid():
        f1.save()
        return redirect('/')
    return render(request,'edit.html',{'edit1':edit1,'f1':f1})