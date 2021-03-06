from django.contrib import admin
from django.urls import path,include
from . import views 

urlpatterns = [
    path("",views.index,name='homepage'),
    path("events",views.events,name='eventpage'),
    path("register",views.register,name='formsub'),
    path("team",views.team,name='teampage'),
    path("achievements",views.achievements,name='achievementpage'),
    path("articles",views.articles,name='articlepage'),
    path("alumni",views.alumni,name='alumnipage'),
    path("suggestion",views.suggestion,name='suggestionsubmission'),
    path("newsletter",views.newsletter,name='newletterpage'),
    path("learning",views.learning,name='peerlearning-page')
]