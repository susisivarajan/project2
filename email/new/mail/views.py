from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def mail(request):
    send_mail("subject","message","susisivarajan@gmail.com",["nifejis299@in2reach.com","susikittu42@gmail.com"],fail_silently=False)
    return HttpResponse("mail send succesfully")
def session(request):
    request.session['sname']="Ram"
    return HttpResponse("user session is set")
def getsession(request):
    sname=request.session['sname']
    return HttpResponse("welcome"+sname)