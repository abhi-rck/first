from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import seeq,faculty,fourthyear,thirdyear,secondyear,firstyear,achievementss
# Create your views here.
def index(request):
    return render(request,'index.html')

def events(request):
    return render(request,'event.html')

def register(request):
    if request.method == "POST":
        name1=request.POST['name1']
        name2=request.POST['name2']
        email=request.POST['email']
        college=request.POST['college']
        mobile=request.POST['phone']
        new=seeq(name1=name1,name2=name2,email=email,college=college,mobile=mobile)
        new.save()
        print('user created')
        return redirect("/events")

def team(request):
    fac=faculty.objects.all()
    fourth=fourthyear.objects.all()
    third=thirdyear.objects.all()
    second=secondyear.objects.all()
    first=firstyear.objects.all()

    return render(request,'team.html',{'fac':fac ,'fourth':fourth,'third':third,'second':second,'first':first})

def achievements(request):
    achievement=achievementss.objects.all()
    return render(request,'achievements.html',{'achievement':achievement})