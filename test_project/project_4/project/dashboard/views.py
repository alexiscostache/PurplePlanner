from django.shortcuts import render,redirect,HttpResponseRedirect
from todo.myfunctions import *
from todo.myForms import CourseCreationForm,AssginmentFormForTeacher,AssginmentFormForStudent
from django.http import JsonResponse
def home(request):
        if(request.user.is_authenticated ):
            myuser=getMyUser(request);
           
            try:
                print("in home")
                myUser=getMyUser(request)
                if(myUser.user_type=="ST"):
                    return student_home(request)
                elif(myUser.user_type=="TR"):
                    return teacher_home(request)
            except Exception as e:
                print(e)
                return render(request,"todo/home.html", {"user_type":"Visitor"})
            

        return redirect("login")


def student_home(request):
      myuser=getMyUser(request)
      todos=getAlltodos(request)
      dones=getAlldones(request)
      overdues=getAlloverdues(request)
      lates=getAlllates(request)
      print(todos)
      return render(request,"dashboard/student_home.html",{"myuser":myuser,"todos":todos,"dones":dones,"overdues":overdues,"lates":lates})


def teacher_home(request):
    myuser=getMyUser(request)
    courses=getAllCourses(request)
    return render(request,"dashboard/teacher_home.html",{"myuser":myuser,"user_type":"TR","courses":courses})

def viewallcourse(request):
      courses=getAllCourses(request)
      return render(request, "dashboard/viewallcourse.html",{"user_type":"TR","courses":courses})
# Create your views here.

def createcourse(request):
    if(request.method=="GET"):
        return render(request,"dashboard/createcourse.html",{"form":CourseCreationForm()});
    else:
        try:
            form=CourseCreationForm(request.POST)
            form.save()
            return redirect("dashboard_home")
        except ValueError:
            return render(request,"dashboard/createcourse.html",{"form":CourseCreationForm(),"error":"wrong inputs"});

 
#viewcourse,viewassignment,grading,createassignment

def viewcourse(request, course_pk):
    course=get_course_or_404_(course_pk,request)
    assignments=get_assignments_from_course(request,course_pk)
    print(assignments)
    dones=get_assignments_from_course_done(request,course_pk)
    print(dones)
    todos=get_assignments_from_course_todo(request,course_pk)
    print(todos)
    return render(request,"dashboard/course.html",{"course":course, "assignments":assignments, "todos":todos, "dones":dones})

def viewassignment(request,course_pk, pk_title):
    assignments=get_assignments_id(request,pk_title)
    print(dir(assignments[0].student.user))
    course=get_course_or_404_(course_pk,request)
    return render(request, "dashboard/assignment.html",{"assignments":assignments,"course":course})

def grading(request, course_pk,pk_title, pk_id):
    assignment=get_assignment_or_404_(request, pk_id)
    if request.method=="POST":
          assignment.grade=request.POST["grade"]
          assignment.save()
    return redirect("viewassignment",course_pk=course_pk,pk_title=pk_title)

def createassignment(request,course_pk):
    if(request.method=="GET"):
        return render(request,"dashboard/createAssignment.html",{"form":AssginmentFormForTeacher()})
    else:

       try:
             form =AssginmentFormForTeacher(request.POST)
             form.save(course_pk,request.POST)
             return redirect("viewcourse",course_pk)
       except ValueError:
            return render(request,"dashboard/createAssignment.html",{"form":AssginmentFormForTeacher(),"error":"wrong value for some fields"})



def student_course(request):
    courses=getAllCourses(request)
    return render(request,"dashboard/student_course.html",{"courses":courses})


def viewalltodo(request):
      myuser=getMyUser(request)
      todos=getAlltodos(request)
      dones=getAlldones(request)
      overdues=getAlloverdues(request)
      lates=getAlllates(request)
      print("all")
      print(todos)
      return render(request,"dashboard/viewalltodo.html",{"myuser":myuser,"todos":todos,"dones":dones,"overdues":overdues,"lates":lates})

def viewtodofromcourse(request,course_pk):
      myuser=getMyUser(request)
      todos=getAlltodos_from_course(request,course_pk)
      dones=getAlldones_from_course(request,course_pk)
      overdues=getAlloverdues_from_course(request,course_pk)
      lates=getAlllates_from_course(request,course_pk)
      print(dones)
      return render(request,"dashboard/viewtodofromcourse.html",{"myuser":myuser,"todos":todos,"dones":dones,"overdues":overdues,"lates":lates})

def completetodo(request,todo_pk):
    todo=get_todo_or_404_(todo_pk,request)
    message="Fail"
    if request.method=="POST":
        message="Success"
        todo.date_complete=timezone.now()
        todo.save()
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
    return JsonResponse({"status":message})

def viewtodo(request, todo_pk):
    todo=get_todo_or_404_(todo_pk,request)
    if request.method=="GET":
        
        print(todo)
        if not todo:
            return render(request, "dashboard/viewtodo.html",{"error":"not found"})
      
        form=AssginmentFormForStudent(instance=todo)
        return render(request, "dashboard/viewtodo.html",{"todo":todo,
                                                     "form": form})
    else:
       try:
             form =AssginmentFormForStudent(request.POST, instance=todo)
             form.save()
             return redirect("dashboard_home")
       except ValueError:
            return render(request,"dashboard/viewtodo.html",{"form":AssginmentFormForStudent(),"error":"wrong value for some fields"})

 