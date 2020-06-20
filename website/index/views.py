from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import seeq,faculty,fourthyear,thirdyear,secondyear,firstyear,achievementss,developers,acphoto,suggest,news,learn
# Create your views here.

def index(request):
    return render(request,'index.html')

def events(request):
    return render(request,'event.html')


def learning(request):
    columns=learn.objects.all()
    eight=learn.objects.filter(col=8)
    five=learn.objects.filter(col=5)
    four=learn.objects.filter(col=4)
    seven=learn.objects.filter(col=7)
    twelve=learn.objects.filter(col=12)
    return render(request,'learning.html',{'columns':columns,'eight':eight,'five':five,'four':four,'seven':seven,'twelve':twelve})


def newsletter(request):
    collapse=news.objects.all()
    return render(request,'newsletter.html',{'collapse':collapse})

def register(request):
    if request.method == "POST":
        name1=request.POST['name1']
        name2=request.POST['name2']
        email=request.POST['email']
        college=request.POST['college']
        mobile=request.POST['phone']
        new=seeq(name1=name1,name2=name2,email=email,college=college,mobile=mobile)
        new.save()
        return redirect("/events")

def team(request):
    fac=faculty.objects.all()
    fourth=fourthyear.objects.all()
    third=thirdyear.objects.all()
    second=secondyear.objects.all()
    first=firstyear.objects.all()
    dev=developers.objects.all()

    return render(request,'team.html',{'fac':fac ,'fourth':fourth,'third':third,'second':second,'first':first, 'dev':dev})

def achievements(request):
    achievement=achievementss.objects.all()
    l=achievementss.objects.filter(var="left")
    r=achievementss.objects.filter(var="right")
    photo=acphoto.objects.all()
    n=len(photo)
    return render(request,'achievements.html',{'achievement':achievement,'achievementl':l,'achievementr':r,'photo':photo,'range':range(0,n)})

def articles(request):
    return render(request,'articlenew.html')

def alumni(request):
    return render(request,'alumni.html')

def suggestion(request):
    name=request.POST['name']
    suggestion=request.POST['suggest']
    new=suggest(name=name,suggestion=suggestion)
    new.save()
    return redirect("/")

