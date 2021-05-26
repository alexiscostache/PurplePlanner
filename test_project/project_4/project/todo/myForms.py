from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from .models import MyUser,Assignments,Courses
from django.forms import ModelForm
from django.utils import timezone

class MyUserAuthenticationForm(AuthenticationForm):
     def __init__(self, *args, **kwargs):
        super(MyUserAuthenticationForm, self).__init__(*args, **kwargs)
        #print(self.fields)
        self.fields['username'].widget.attrs.update({'class' : 'form-control'})
        self.fields['password'].widget.attrs.update({'class' : 'form-control'})

class MyUserCreateForm(UserCreationForm):
    STUDENT="ST"
    TEACHER="TR"
    PRINCIPAL="PL"
    VISITOR="VR"
    USER_TYPES=[
        (STUDENT,"Student"),
        (TEACHER,"Teacher"),
        (PRINCIPAL,"Principal"),
        (VISITOR,"Visitor")
        ]

    user_type=forms.ChoiceField(choices=USER_TYPES)

    class Meta:
        model = User
        fields=("username","email","password1","password2","user_type")

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")
        user = super(UserCreateForm, self).save(commit=True)
        user_profile = MyUser(user=user, user_type=self.cleaned_data['user_type'])
        user_profile.save()
        return user, user_profile

class AssginmentFormForStudent(ModelForm):
      class Meta:
        model=Assignments
        fields=["progress", "date_complete","importance"]

class AssginmentFormForGrading(ModelForm):
      class Meta:
        model=Assignments
        fields=["grade"]
class AssginmentFormForTeacher(ModelForm):
    
      class Meta:
        model=Assignments
        fields=["title", "description"]
      def save(self,course_id, post,commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")
       # user = super(UserCreateForm, self).save(commit=True)
        course=Courses.objects.filter(id=course_id).get()
        if(course):
            students=MyUser.objects.filter(user_type="ST",courses=course)
           # print(len(students))

            title=post["title"]
            description=post["description"]
            date_due=post["date_due"]

            for student in students:
                Assignments.objects.create(
                                                course=course,
                                                student=student,
                                                title=title,
                                               description=description,
                                               date_start=timezone.now(),
                                               date_due=date_due,
                                      

                                               )
            return 


class CourseCreationForm(ModelForm):
       class Meta:
        model=Courses
        fields=["title", "description","users"]
