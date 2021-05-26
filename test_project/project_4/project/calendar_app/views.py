from django.shortcuts import render
from django.http import JsonResponse
from todo.myfunctions import getAlltodos,getMyUserById,getAllFromStudent,getAllAssignmentsFromStudent,getAllAssignmentsFromStudent2
from todo.models import Assignments

def calendar_test(request):
  
    if request.method=="POST" or True:
        print(request.POST)
        print(request.user)
        id=getMyUserById;
    data=getAllAssignmentsFromStudent(request)
    #data=getAllAssignmentsFromStudent(getMyUserById(46))
    #data=serializers.serialize("json",list(data))
    print(data.filter(title="f").values("date_complete"))
    return JsonResponse({"status":"Success","todos":list(data)})


