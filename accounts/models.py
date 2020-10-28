from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):  
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    User_Name = models.CharField(max_length=20) 
    Email = models.CharField(max_length=40) 
    Password  = models.CharField(max_length=20)  
    class Meta:  
        db_table = "Student"  
    def __str__(self):
        return self.User_Name        