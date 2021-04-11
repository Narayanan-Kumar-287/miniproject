from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def teachers(request):
    return render(request, "index.html")

def student(request):
    return render(request, "student.html")

def login(request):
    return render(request, "login.html")        

def submit(request):
    if request.method == 'POST':
        time = request.POST.get('time','')
        subject = request.POST.get('subject','')
        message = request.POST.get('message','')
        content=''' Subject : {0}
        Time : {1}
        Message : {2}'''.format(subject,time,message)

        send_mail(
            subject,
            content,
            'christijkmoodle@gmail.com',
            ['athul11321@gmail.com','narayanank2001@gmail.com','josmiajose123@gmail.com','godwinjoyijk@gmail.com'],
            )
        
        return render(request, 'index.html',{time:'time',message:'message',subject:'subject'})
        
    
    else:
        return render(request, 'index.html',{})

# Create your views here.
