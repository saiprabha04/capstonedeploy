from django.db import models
from accounts.models import Student

class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    photo = models.ImageField(null=True)
    date_created = models.DateField(auto_now_add=True,null=True)
    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
    
class Content(models.Model):
    subject=models.ForeignKey(Subject,null=True,on_delete=models.SET_NULL)
    nameofsite=models.TextField()
    link=models.TextField()
    description=models.TextField()
    


class Enroll(models.Model):
    STATUS = (
        ('Inactive','Inactive'),
        ('Active','Active'),
    )
    subject = models.ForeignKey(Subject,null=True,on_delete=models.SET_NULL)
    student = models.ForeignKey(Student,null=True,on_delete=models.SET_NULL)
    status = models.CharField(max_length=200,null=True,choices=STATUS)
    date_modified = models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return str(self.student)+'\'s'+' '+str(self.subject)

            
