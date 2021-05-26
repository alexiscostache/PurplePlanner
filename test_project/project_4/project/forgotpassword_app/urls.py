from django.urls import path
from .views import home_view,forgotpasswordsucces,newpassword,passwordchanged
urlpatterns = [
    path("",home_view, name="forgot_password"),
    path("success/",forgotpasswordsucces, name="forgotpasswordsucces"),
    path("newpassword/",newpassword, name="newpassword"),
    path("passwordchanged/",passwordchanged, name="passwordchanged"),

 
    
    ]