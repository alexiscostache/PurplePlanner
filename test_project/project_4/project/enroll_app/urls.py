from django.urls import path
from .views import home_view,enroll_course
urlpatterns = [
    path("",home_view, name="enrollment"),
    path("enroll/<int:course_id>",enroll_course, name="enroll_course"),
 
    
    ]