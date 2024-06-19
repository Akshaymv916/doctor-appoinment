from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from app.models import Appoinment, Department, Doctor, Time


@login_required(login_url='login')
def index(request):
    department=Department.objects.all()
    history=Appoinment.objects.filter(owner_user=request.user)

    time=Time.objects.all()

    context={
        'department':department,
        'time':time,
        'history':history

    }
    return render(request,'index.html',context)

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        email=request.POST ['email']
        username=request.POST['username']
        password=request.POST['password']
        password2=request.POST['password2']

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()

                user_login=auth.authenticate(username=username,password=password)
                auth.login(request,user_login)
                return redirect('login')
        else:
            messages.info(request,'password not match')
            return redirect('signup')
    else:
        return render(request,'signup.html')
    

def logout(request):
    auth.logout(request)
    return redirect('login')

def get_doctor(request):
    department_id = request.GET.get('department_id')
    doctors = Doctor.objects.filter(department_id=department_id).values('id','name')
    return JsonResponse({'doctors': doctors})



def appoinment(request):
        if request.method=='POST':
            department=request.POST['department']
            date=request.POST ['date']
            time=request.POST ['time']
            name=request.POST ['name']
            phone=request.POST ['phone']
            message=request.POST ['message']
            appo=Appoinment(owner_user=request.user,name=name,department=department,date=date,Time=time,phone=phone,msg=message)
            appo.save()
            messages.success(request,'appoinment send successfully and wait for response')
            return redirect('/')

def clear(request):
        history=Appoinment.objects.filter(owner_user=request.user)
        history.delete()
        return redirect('/')

