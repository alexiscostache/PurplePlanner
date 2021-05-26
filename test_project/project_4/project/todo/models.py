from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

class MyUser(models.Model):
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

    user_type=models.CharField(max_length=15, choices=USER_TYPES, default=VISITOR)
    image=models.ImageField(upload_to="portfolio/images/",blank=True,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
   
    def __str__(self):
        return self.user_type+" "+self.user.username

class Courses(models.Model):
    users=models.ManyToManyField(MyUser)
    title=models.CharField(max_length=200)
    description=models.TextField()

    def __str__(self):
        return self.title

class Assignments(models.Model):
    course=models.ForeignKey(Courses,on_delete=models.CASCADE)
    student=models.ForeignKey(MyUser,on_delete=models.CASCADE,)
    title=models.CharField(max_length=200)
    description=models.TextField()
    date_start=models.DateTimeField()
    date_due=models.DateTimeField()
    date_complete=models.DateTimeField(blank=True,null=True)
    progress=models.FloatField(default=0)
    grade=models.FloatField(blank=True,null=True)
    date_grade=models.DateTimeField(blank=True,null=True)
    importance=models.IntegerField(default=0, validators=[MinValueValidator(-1),MaxValueValidator(100)])
    attemps=models.IntegerField(default=3, validators=[MinValueValidator(0),MaxValueValidator(10)])

    def __str__(self):
        return self.title




 

