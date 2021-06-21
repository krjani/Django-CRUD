from django.shortcuts import render
from enroll.forms import Student
from enroll.models import User
from django.http import HttpResponseRedirect
# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = Student(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            data = User(name=nm,email=em,password=pw)
            data.save()
            fm = Student()
    else:
        fm = Student()
    student = User.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'std':student})

# this function will delete data

def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

#  this function will update data

def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = Student(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        # will give editing options
        pi = User.objects.get(pk=id)
        fm = Student(instance=pi)

    return render(request,'enroll/update.html',{'form':fm})
    