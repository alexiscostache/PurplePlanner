from django.shortcuts import render,redirect
from django.http import JsonResponse
from todo.myfunctions import getAllAssignmentsFromStudent,getAllAssignmentsFromStudent2,sortAssignmentsByCourse,getRecentGrade,getMyUser
import random
from django.utils import timezone
from django.db.models import Count
from django.core.files.storage import FileSystemStorage
from django.conf import settings
def update_grade_test(request):
    todos=getAllAssignmentsFromStudent2(request)
    for todo in todos:
        todo.grade=grade=random.randint(50,100)
        todo.date_grade=timezone.now()
        todo.save()
    
    print(todos)
    return todos
 

def sortedbygroup(todos):
    todos_=todos.values("course__title").annotate(ccount=Count("course"))
    #print(todos_)

def profile_home(request):
   # todos=getAllAssignmentsFromStudent(request)
    #sortedbygroup(todos)
    #print(todos)
    #update_grade_test(request)
   
    #print(getRecentGrade(request))
    myuser=getMyUser(request)
    print("image: ",myuser.image)
    return render(request,"profile_app/profile_test.html",{"image":myuser.image})

def get_data(request):
    print(request.GET)
    todos_course= sortAssignmentsByCourse(request)
    return JsonResponse({"message":"hello","data":todos_course,"recent":getRecentGrade(request)})
# Create your views here.
def upload_image(request):
    if request.method=="POST":
        print("upload image: ",request.POST.get("image"))
        print("upload: ",request.FILES["image"])
        uploaded_file=request.FILES["image"]
        fs=FileSystemStorage()
        name_file=fs.save(uploaded_file.name,uploaded_file)
        myuser=getMyUser(request)
        print(fs.url(name_file))
        myuser.image=fs.url(name_file)
        myuser.save()
   
    return redirect("profile_home")