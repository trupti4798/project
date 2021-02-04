from django.shortcuts import render

from django.shortcuts import render, redirect  
from student.forms import StudentForm  
from student.models import Student  
# Create your views here. 
def index(request):
	#return HttpResponse("<h2>welcome to all!!!!</h2>") 
	return render(request,'index.html')

def new(request):  
    if request.method == "POST":  
        form = StudentForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = StudentForm()  
    return render(request,'new.html',{'form':form})
    

def show(request):  
    student = Student.objects.all()  
    return render(request,"show.html",{'student':student}) 

def edit(request, id):  
    student = Student.objects.get(id=id)  
    return render(request,'edit.html', {'student':student}) 


def update(request, id):  
    student = Student.objects.get(id=id)  
    form = StudentForm(request.POST, instance = student)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'student': student}) 

def destroy(request, id):  
    student = Student.objects.get(id=id)  
    student.delete()  
    return redirect("/show")


# Create your views here.
