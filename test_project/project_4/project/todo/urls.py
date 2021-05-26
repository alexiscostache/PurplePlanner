from django.urls import path
from .views import home,loginuser,signupuser, logoutuser,student_home,teacher_home,dashboard,profile
urlpatterns = [
    path('', home, name="home"),
    path('home/', home, name="home"),
    path('login/', loginuser, name="login"),
    path('signup/', signupuser, name="signup"),
    path('logout/', logoutuser, name="logout"),
    path('student_home/', student_home, name="student_home"),
    path('teacher_home/', teacher_home, name="teacher_home"),
  
   
    path("dashboard",dashboard),
    
]
