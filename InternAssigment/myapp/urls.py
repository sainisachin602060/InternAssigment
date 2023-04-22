from django.contrib import admin
from django.urls import path
from . import views


#make two route here
#first route save our data into database
#second route display the data on display page
urlpatterns = [
    path('',views.studentFrom,name="studentFrom"),
    path('display/',views.display,name="display"),
    
    
]
