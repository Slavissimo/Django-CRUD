from django.shortcuts import render, redirect
from .models import Student
# Create your views here.
def index(request):
    data = Student.objects.all()
    context = {"data" : data}
    return render(request, "index.html" , context)

def deleteData(request, id):
   
   d = Student.objects.get(id=id)
   d.delete()

   return redirect("/")

def updateData(request, id):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']

        edit = Student.objects.get(id=id)
        edit.name = name
        edit.email = email
        edit.age = age
        edit.save()
        return redirect("/")
    d = Student.objects.get(id=id)
    context = {"d" : d}

    return render(request, "edit.html" , context)

def insertData(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        query=Student(name=name, email=email, age=age)
        query.save()
        return redirect("/")

    return render(request, "index.html")