from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from .forms import *
import json
from django.contrib.auth.models import User


def home(request):
    if request.session.has_key('uid'):

        subjects = Subject.objects.all()
        students = Student.objects.all()
        enrolls = Enroll.objects.all()
        total_courses = subjects.count()
        total_students = students.count()
        active = Enroll.objects.filter(status="Active").count()
        total_enrolls = enrolls.count()
        stucourse_enrolls=""
        searchfilter=""
        
        if request.user.is_staff:
            userr = User.objects.get(username=request.user)
        else:
            print(request.user)
            userr = Student.objects.get(User_Name=request.user)
            stucourse_enrolls =  userr.enroll_set.all()
        context = {'subjects':subjects,'students':students,'enrolls':enrolls,'total_courses':total_courses,'total_students':total_students,'active':active,'total_enrolls':total_enrolls,'userr':userr,'stucourse_enrolls':stucourse_enrolls}
        return render(request,'dash.html',context)
    else:
        return redirect('login')

def about(request):
    return render(request,'about.html')


def contents(request,pk):
    contents=Content.objects.get(subject=pk) 
    context={'content':contents}
    return render(request,'content.html',context)

def list(request):
    subjects = Subject.objects.all().order_by('title') 
    context = {'subjects':subjects}             
    return render(request,'courses/list.html',context)

def contact(request):
    return render(request,'contact.html')
    

def enroll_course(request):
    data = json.loads(request.body)
    subjectid = data['subjectid']
    student = Student.objects.get(User_Name=request.user)
    subject = Subject.objects.get(id = subjectid)
    enroll = Enroll.objects.get_or_create(subject=subject,student=student,status="Inactive")
    return JsonResponse("Enrolled a course", safe=False)   

def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CourseForm()        
    context ={'form':form}        
    return render(request,'course_form.html',context)

def update_enroll(request, pk):
    enrolls = Enroll.objects.get(id=pk)
    if request.method == 'POST':
        form = EnrollForm(request.POST, instance=enrolls)
        if form.is_valid():
            form.save()
            enrolls.delete()
            return redirect('home')
    else:
        form = EnrollForm(instance=enrolls)                
    context ={'form':form}        
    return render(request,'enroll_form.html',context)

def remove_enroll(request, pk):
    enrolls = Enroll.objects.get(id=pk)
    form = EnrollForm(instance=enrolls) 
    if request.method == 'POST':
        enrolls.delete()  
        return redirect('home')
    context = {'enrolls':enrolls, 'form':form}
    return render(request,'deleteform.html',context)     


def remove_uenroll(request, pk):
    enrolls = Enroll.objects.get(id=pk)
    form = EnrollForm(instance=enrolls) 
    if request.method == 'POST':
        enrolls.delete()  
        return redirect('home')
    context = {'enrolls':enrolls, 'form':form}
    return render(request,'deleteform.html',context)     
####################################
def best():
     enrolls = Enroll.objects.all()
     max = 0
     sub=[]
     bestseller = "Django"   
     for i in range(0,len(enrolls)):
         sub.append(enrolls[i].subject)

     counts = dict() 
     for subj in sub:
         if subj in counts:
             counts[subj] += 1
         else:
             counts[subj] = 1
     for key in counts:
         if max < counts[key]:
             max = counts[key]
             bestseller = key 
     return bestseller          
##############################
def hp(request):
    bestseller="Django"
    bestsellr = Subject.objects.get(title=bestseller)
    context = {'bestsellr':bestsellr}       
    return render(request,'hp.html',context)

def search(request):
    query = request.GET['query']
    search_content = Subject.objects.filter(title__icontains=query)
    context = {'search_content':search_content,'query':query}
    return render(request,'search.html',context)
