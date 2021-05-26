from django.shortcuts import render, HttpResponseRedirect
from todo.myfunctions import getAllAvailableCourses,createAssignmentForStudent

def home_view(request):
    courses=getAllAvailableCourses(request)
    #print(courses[0].users)
    return render(request,"enroll_app/index.html",{"courses":courses})


def enroll_course(request,course_id):
    
    createAssignmentForStudent(request,course_id)
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)
# Create your views here.
