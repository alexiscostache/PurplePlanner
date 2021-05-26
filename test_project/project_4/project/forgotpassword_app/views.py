from django.shortcuts import render,redirect
from todo.myfunctions import findEmail,findUserThroughEmail
from django.core.mail import send_mail
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
def home_view(request):

    if request.method=="POST":
        print()
        print("results: ",)
        message_name="purple planner forgot password"
        message_to_email=request.POST.get("email")
        chanage_password=request.scheme+"://"+request.META['HTTP_HOST']+reverse("newpassword")
        message="change password:\n "+chanage_password
        message_from_email="PurplePlannerZ10@gmail.com"
        user=findUserThroughEmail(message_to_email)
         
        if user:
            send_mail(
                message_name,
                message,
                message_from_email,
                [message_to_email]
                
                )
            print(user)
            login(request,user)
          
            return redirect("forgotpasswordsucces")

        return render(request,"forgotpassword_app/forgotpassword.html",{"error":"wrong email"})

    return render(request,"forgotpassword_app/forgotpassword.html",{"error":""})

def forgotpasswordsucces(request):
    return render(request,"forgotpassword_app/forgotpasswordsucces.html")
@login_required
def newpassword(request):
    if request.method=="POST":
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")
        if(password1==password2):
            print("change password")
            request.user.set_password(password2)
            request.user.save()
            return redirect("passwordchanged")
        return render(request,"forgotpassword_app/newpassword.html",{"error":"passwords do not match!"})

    return render(request,"forgotpassword_app/newpassword.html",{"error":""})
def passwordchanged(request):
    return render(request,"forgotpassword_app/passwordchanged.html")

# Create your views here.
