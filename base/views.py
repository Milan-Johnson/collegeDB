from django.shortcuts import render
from django.http import HttpResponse
from .models import*

# Create your views here.
def home(request):
    department = Department.objects.all()
    # print(department)
    # for item in allDepartments:
    #    print(allDepartments.department)
    # context = {'department':department}
    
   
    return HttpResponse(department)
    # return render(request, 'home.html', context)

def room(requset):
    return render(requset , 'room.html')