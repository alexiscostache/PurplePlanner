from django.shortcuts import render,redirect, get_object_or_404
from .models import MyUser
from django.contrib.auth.models import User
from .myfunctions import *
from .myForms import MyUserCreateForm,AssginmentFormForStudent,AssginmentFormForGrading,AssginmentFormForTeacher,MyUserAuthenticationForm
from django.db import IntegrityError
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from dashboard.views import home as new_dashboard
from django.utils import timezone
# Create your views here.

def home(request):
    #print(dir(MyUser.objects))
   # print(dir(User.objects))
  #  createUsers(10)
    #delete_users()
    #createAssignments()
    if(request.user.is_authenticated ):
        try:
            #print("home")
            
            return new_dashboard(request)
       
        except Exception as e:
           # print(e)
            return render(request,"todo/home.html", {"user_type":"Visitor"})
       
    

    return redirect("login")

def loginuser(request):
    if request.user.is_authenticated:
       return redirect("/home")
   # print("login")
    if request.method== "GET":
        form=MyUserAuthenticationForm()
     #   print(form.fields)
        return render(request,"todo/login.html",{"form":MyUserAuthenticationForm()})
    else:
        user=authenticate(request,
                      username=request.POST["username"],
                      password=request.POST["password"])
        if user is None:
              return render(request, 
                  "todo/login.html",
                  {"form":AuthenticationForm(),
                   "error":"Username and password did not match"
                   })
        else:
              login(request,user)
              return redirect("/home")


def signupuser(request):

    if request.method== "GET":
        return render(request,"todo/signup.html",{"form":MyUserCreateForm()})
    else:

        if request.POST["password1"]==request.POST["password2"]:
            try: 
                user=User.objects.create_user(request.POST["username"],
                                              request.POST["email"],
                                              request.POST["password1"]
                                              
                                              )
                user.save()
                login(request,user)
                myuser=MyUser.objects.create(user_type= request.POST["user_type"],
                                             user=user)
                myuser.save()
                return redirect("/home")
            except IntegrityError:
               return render(request,"todo/signup.html",
                             
                             {"form":MyUserCreateForm(),
                              "error":"user name already exited"
                              })
        return render(request,"todo/signup.html",
                             
                             {"form":MyUserCreateForm(),
                              "error":"different passwords"
                              })

def logoutuser(request):
        if(request.method=="POST"):
          logout(request)
        return redirect("/home")
        
    
def student_home(request):
    
      return student_dashboard(request)


def teacher_home(request):
      courses=getAllCourses(request)
      return render(request, "todo/home.html",{"user_type":"TR","courses":courses})
    

def completetodo(request,todo_pk):
    todo=get_todo_or_404_(todo_pk,request)
    if request.method=="POST":
        todo.date_complete=timezone.now()
        todo.save()
    return redirect("/home")

def viewtodo(request, todo_pk):
    todo=get_todo_or_404_(todo_pk,request)
    if request.method=="GET":
        
     #   print(todo)
        if not todo:
            return render(request, "todo/viewtodo.html",{"error":"not found"})
      
        form=AssginmentFormForStudent(instance=todo)
        return render(request, "todo/viewtodo.html",{"todo":todo,
                                                     "form": form})
    else:
       try:
             form =AssginmentFormForStudent(request.POST, instance=todo)
             form.save()
             return redirect("/home")
       except ValueError:
            return render(request,"todo/viewtodo.html",{"form":AssginmentFormForStudent(),"error":"wrong value for some fields"})

 
def viewcourse(request, course_pk):
    course=get_course_or_404_(course_pk,request)
    assignments=get_assignments_from_course(request,course_pk)
  #  print(assignments)
    dones=get_assignments_from_course_done(request,course_pk)
 #   print(dones)
    todos=get_assignments_from_course_todo(request,course_pk)
 #   print(todos)
    return render(request,"todo/course.html",{"course":course, "assignments":assignments, "todos":todos, "dones":dones})

def viewassignment(request,course_pk, pk_title):
    assignments=get_assignments_id(request,pk_title)
  #  print(dir(assignments[0].student.user))
    course=get_course_or_404_(course_pk,request)
    return render(request, "todo/assignment.html",{"assignments":assignments,"course":course})


def grading(request, course_pk,pk_title, pk_id):
    assignment=get_assignment_or_404_(request, pk_id)
    if request.method=="POST":
          assignment.grade=request.POST["grade"]
          assignment.date_grade=timezone.now()
          assignment.save()
    return redirect("viewassignment",course_pk=course_pk,pk_title=pk_title)

def createassignment(request,course_pk):
    if(request.method=="GET"):
        return render(request,"todo/createAssignment.html",{"form":AssginmentFormForTeacher()})
    else:

       try:
             form =AssginmentFormForTeacher(request.POST)
             form.save(course_pk,request.POST)
             return redirect("viewcourse",course_pk)
       except ValueError:
            return render(request,"todo/createAssignment.html",{"form":AssginmentFormForTeacher(),"error":"wrong value for some fields"})



def dashboard(request):
    return render(request,"todo/dashboard-test.html")


def profile(request):
      return render(request,"todo/profile-test.html")



