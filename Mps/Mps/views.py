from django.http import HttpResponse
from django.shortcuts import render,HttpResponseRedirect, redirect
from Mpsapp.models import Teachers,Gallery_main,Gallery

def home(request):
    Gal_main = Gallery_main.objects.all()
    return render(request,"mps.html",{"Title":"Welcome to MPS","Gal_main":Gal_main})

def schoolinfo(request):
    return render(request,"schoolinfo.html",{"Title":"About MPS"})

def vision(request):
    return render(request,"vision.html",{"Title":"Vision of MPS"})

def mission(request):
    return render(request,"mission.html",{"Title":"Mission of MPS"})

def directormessage(request):
    return render(request,"directormessage.html",{"Title":"MPS Director Message"})

def principalmessage(request):
    return render(request,"principalmessage.html",{"Title":"MPS Principal Message"})

def infrastructure(request):
    return render(request,"infrastructure.html",{"Title":"Infrastructure of MPS"})

def playschool(request):
    return render(request,"playschool.html",{"Title":"Our Play School"})

def primaryschool(request):
    return render(request,"primaryschool.html",{"Title":"Our Primary School"})

def secondaryschool(request):
    return render(request,"secondaryschool.html",{"Title":"MPS Secondary School"})

def cocurricular(request):
    return render(request,"cocurricular.html",{"Title":"Cocurricular Activities In MPS"})

def sports(request):
    return render(request,"sports.html",{"Title":"Sports In MPS"})

def visualarts(request):
    return render(request,"visualarts.html",{"Title":"Visual Arts In MPS"})

def paintings(request):
    return render(request,"paintings.html",{"Title":"Painting In MPS"})

def ourteachers(request):
    Teacher = Teachers.objects.all()
    return render(request,"ourteachers.html",{"Title":"Teachers of MPS","Teach":Teacher})

def gallery(request):
    Gal = Gallery.objects.all()
    return render(request,'gallery.html',{"Title":"MPS Moments","Gal":Gal})

def contact(request):
    return render(request,'contact.html',{"Title":"Welcome : Reach Us",})

def login(request):
    return render(request,'Login.html',{"Title":"Login to MPS"})

def signup(request):
    return render(request,"SignUp.html",{"Title":"SignUp to MPS"})