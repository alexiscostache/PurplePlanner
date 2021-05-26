from .models import MyUser,Courses,Assignments
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.db.models import F,Count,Q,Avg
import random
FIRST_NAME=[ "Archer", "Brooks", "Carter", "Fletcher", "Graham", "Huxley", "Mason", "Reed", "Sawyer", "Wilder"]
SECOND_NAME=["Smith","Johnson","Williams","Jones","Brown","Davis","Miller","Wilson"]
def password_generator(length=8):
    characters=list("abcdefghijklmnopqystuvwxyz")
    thepassword=""
  
    characters+=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    characters+=list("0123456789")

    characters+=list(",./")
    for x in range(int(length)):
        thepassword+=random.choice(characters)
   
    return thepassword

def delete_users():
    User.objects.all().delete()


def createUsers(n):
    for i in range(n):
        firstname=random.choice(FIRST_NAME)
        seoncdname=random.choice(SECOND_NAME)
        username=firstname+"_"+seoncdname+str(i)
        email=username+"@gmail.com"
        password=password_generator()
        user=User.objects.create_user(username=username,
                                      email=email,
                                      password=password,
                                      first_name=firstname,
                                      last_name=seoncdname
                                      )
        user.save()
        myuser=None
        if(i>=n-2):
                  myuser=MyUser.objects.create(user_type="TR",user=user)
        else:
             myuser=MyUser.objects.create(user_type="ST",user=user)
        myuser.save()


def createAssignments(n=5):
   # Assignments.objects.all().delete()
    for course in Courses.objects.all():
        students=MyUser.objects.filter(user_type="ST",courses=course)
       #print(len(students))
        
        for i in range(n):
                title=course.title+"_"+str(i)
                date_due=timezone.now()+timedelta(random.randint(5,30))
                importance=random.randint(0,100)
                for student in students:
                                Assignments.objects.create(
                                            course=course,
                                            student=student,
                                            title=title,
                                           description="ha",
                                           date_start=timezone.now(),
                                           date_due=date_due,
                                           progress=0,
                                           importance=importance

                                           )
    pass


def getMyUser(request):
 #   print(MyUser.objects.filter(user=request.user))
    return MyUser.objects.filter(user=request.user).get()

def getMyUserById(id):
     return MyUser.objects.filter(id=id).get()

def getAllFromStudent(user):
    student=getMyUser(user)
    return Assignments.objects.filter(student=student).all()

def getAllAssignmentsFromStudent2(user):
       student=getMyUser(user)
       return Assignments.objects.filter(student=student).all()
def getAllAssignmentsFromStudent(user):
    student=getMyUser(user)
    return Assignments.objects.filter(student=student).values("title",
                                                              "id",
                                                              "course__title",
                                                              "course__id",
                                                              "date_start",
                                                              "date_due",
                                                              "date_complete",
                                                              "grade",
                                                              "progress",
                                                              "description",
                                                              "importance")

def average_grade(todos):
    sum_=sum([todo["grade"] for todo in todos if todo["grade"]])
    length=len([todo["grade"] for todo in todos if todo["grade"]])
    if(length==0):
        return 0
    return sum_/length

def sortAssignmentsByCourse(request):
    todos=getAllAssignmentsFromStudent2(request)
    todos_course=list(todos.values("course__title","course__id").annotate(number_assignment=Count("course")))

    todos_sorted={}
   # print(todos_course)
    for course in todos_course:
        course["assignments"]=list(todos.filter(course__title=course["course__title"]).values("title","id", "date_start",
                                                              "date_due",
                                                              "date_complete","grade"))
        course["assignments_status"]={ "todo":len(getAlltodos_from_course(request,course["course__id"])),
                                      "done":len(getAlldones_from_course(request,course["course__id"])),
                                      "overdue":len(getAlloverdues_from_course(request,course["course__id"])),
                                      "late": len(getAlllates_from_course(request,course["course__id"]))

            
            
            }
        course["grades"]=[grade["grade"] for grade in   list(todos.filter(course__title=course["course__title"]).values("grade").order_by("date_grade"))]
        course["average_grade"]=average_grade(course["assignments"])



   # print(todos.aggregate(Avg('grade')))
   # print(todos.values("grade"))
 #   print(*["average_grade: "+ str(course["average_grade"]) for course in todos_course],sep='\n')
  #  print(*["assignments_status: "+ str(course["assignments_status"]) for course in todos_course],sep='\n')
 #   print(*["grades: "+ str(course["grades"]) for course in todos_course],sep='\n')
 #   print(*["number_assignment: "+ str(course["number_assignment"]) for course in todos_course],sep='\n')
    return todos_course

        
def getRecentGrade(request):
    todos=getAllAssignmentsFromStudent2(request)
    todos_=list(todos.filter(date_grade__isnull=False).values("title","id","grade","date_grade").order_by("date_grade"))
    if(todos_.__len__()>=5):
        return todos_[:5]
    else:
        return todos_
        



def getAlltodos(user):
    student=getMyUser(user)
    return Assignments.objects.filter(student=student, date_complete__isnull=True).filter( date_due__gt=timezone.now()).all()

def getAlldones(user):
    student=getMyUser(user)
    return Assignments.objects.filter(student=student, date_complete__isnull=False).filter(date_complete__lt=F("date_due")).all()

def getAlloverdues(user):
    student=getMyUser(user)
    return Assignments.objects.filter(student=student, date_complete__isnull=True).filter( date_due__lt=timezone.now()).all()
def getAlllates(request):
     student=getMyUser(request)
     return Assignments.objects.filter(student=student,date_complete__isnull=False).filter(date_complete__gt=F("date_due")).all()

def getAlltodos_from_course(request,course_id):
     student=getMyUser(request)
     return Assignments.objects.filter(student=student,course_id=course_id, date_complete__isnull=True).filter( date_due__gt=timezone.now()).all()


def getAlldones_from_course(request,course_id):
    student=getMyUser(request)
    return Assignments.objects.filter(student=student,course_id=course_id,date_complete__isnull=False).filter(date_complete__lt=F("date_due")).all()

def getAlloverdues_from_course(request,course_id):
    student=getMyUser(request)
    return Assignments.objects.filter(student=student,course_id=course_id, date_complete__isnull=True).filter( date_due__lt=timezone.now()).all()

def getAlllates_from_course(request,course_id):
     student=getMyUser(request)
     return Assignments.objects.filter(student=student,course_id=course_id,date_complete__isnull=False).filter(date_complete__gt=F("date_due")).all()

def get_todo_or_404_(pk_id,request):
    return get_object_or_404(Assignments,pk=pk_id, student=getMyUser(request))
def getAllAvailableCourses(request):
     users=getMyUser(request)
     return Courses.objects.exclude(users=users).all()

def getAllCourses(request):
    users=getMyUser(request)
    return Courses.objects.filter(users=users).all()

def createAssignmentForStudent(request,course_id):
    user=getMyUser(request)
    course=Courses.objects.filter(id=course_id).get()
    course.users.add(user)

    assignments=Assignments.objects.filter(course__id__exact=course_id).all().annotate(Count("title"))
   # print(assignments)
    for assignment in assignments:
        importance=random.randint(0,100)
        Assignments.objects.create(
                                            course=course,
                                            student=user,
                                            title=assignment.title,
                                           description=assignment.description,
                                           date_start=assignment.date_start,
                                           date_due=assignment.date_due,
                                           progress=0,
                                           importance=importance

                                           )

    
   
   

def get_course_or_404_(course_pk,request):
     return get_object_or_404(Courses,pk=course_pk, users=getMyUser(request))

def get_assignments_from_course(request, course_pk):
     return Assignments.objects.filter(course__id=course_pk, student__user_type="ST").values("title").annotate(Count("title"))

def get_assignments_from_course_todo(request, course_pk):
     return Assignments.objects.filter(course__id=course_pk, student__user_type="ST",date_due__gte=timezone.now() ).values("title").annotate(Count("title"))
def get_assignments_from_course_done(request, course_pk):
     return Assignments.objects.filter(course__id=course_pk, student__user_type="ST", date_due__lt=timezone.now() ).values("title").annotate(Count("title"))

def get_assignments_id(request,pk_title):
     title=pk_title
     return Assignments.objects.filter(title=title).all()

def get_assignment_or_404_(request,pk_id):
    return get_object_or_404(Assignments,pk=pk_id)

def findEmail(email):
    return len(User.objects.filter(email=email).all())
def findUserThroughEmail(email):
    if findEmail(email):
        return User.objects.filter(email=email).all()[0];
    return None