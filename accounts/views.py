from django.shortcuts import render,redirect
from django.template import Context, loader
from django.http import HttpResponse
from accounts.forms import StudentForm

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, auth
from django.contrib.auth.models import User
from django.contrib.auth.views import *
from django.contrib import messages

def forgot_password(request):
    if request.method == 'POST':
        return password_reset(request, 
            from_email=request.POST.get('email'))
    else:
        return render(request, 'forgot_password.html')




def signup(request):
    if request.method == 'POST':
        stu = StudentForm(request.POST)
        if stu.is_valid():
            user = User.objects.create_user(username=stu.cleaned_data['User_Name'],
                                            password=stu.cleaned_data['Password'],
                                            email=stu.cleaned_data['Email'])

            user.save()
            stu.save()
            messages.add_message(request,messages.SUCCESS, "You Have Registered")
            return redirect('login')
    else:
        stu = StudentForm()
    return render(request,'signup.html',{'form':stu})


def student(request):
    return render(request,'student/student.html')   

def login(request):
    if request.method=='POST':        
            username=request.POST['username']
            password=request.POST['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                request.session['uid']=request.POST['username']
                auth.login(request,user)
                if request.POST.get("check"):
                    template = loader.get_template("index.html")
                    response=HttpResponse(template.render())
                    response.set_cookie('username',username)
                    response.set_cookie('password',request.POST['password'])
                    return response
                  
                return redirect('home')
            else:
                messages.info(request,"Invalid Credentials")
                return redirect("login")
    else:
        if request.COOKIES.get('username'):
             return render(request,'login.html',{'un':request.COOKIES['username'],'pw':request.COOKIES['password']})
        else:
            return render(request,'login.html')

