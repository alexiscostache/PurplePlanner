from django.urls import path
from .views import home,viewallcourse,createcourse,viewcourse,viewassignment,grading,createassignment,viewtodo,completetodo,viewalltodo,student_course,viewtodofromcourse
urlpatterns = [
    path('', home, name="dashboard_home"),
     path("courses/",viewallcourse,name="viewallcourse"),
     path("course/createcourse",createcourse,name="createcourse"),
      path("course/<int:course_pk>",viewcourse,name="viewcourse"),
    path("course/<int:course_pk>/createassignment",createassignment,name="createassignment"),
    path("course/<int:course_pk>/assignment/<str:pk_title>",viewassignment,name="viewassignment"),
    path("course/<int:course_pk>/assignment/<str:pk_title>/grading/<int:pk_id>",grading,name="grading"),
      path("todo/<int:todo_pk>",viewtodo,name="viewtodo"),
    path("todo/<int:todo_pk>/complete",completetodo,name="completetodo"),
    path("todos/",viewalltodo,name="viewalltodo"),
    path("student_course/",student_course,name="student_course"),
    path("student_course/<int:course_pk>/",viewtodofromcourse,name="viewtodofromcourse"),

]
