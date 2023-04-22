from django.shortcuts import render,redirect
from .models import StudentMarks


def studentFrom(request):
    if request.method=='POST':
        #fetch the all data from html field
        Name=request.POST['Name']
        Dob=request.POST['Dob']
        PhysicsMarks=request.POST['PhysicsMarks']
        ChemistryMarks=request.POST['ChemistryMarks']
        CsMarks=request.POST['CsMarks']
        
        #surround with try and except for error handling
        #save the student data into databse using orm queries
        
        try:
            StudentObj=StudentMarks(Name=Name,DOb=Dob,PhysicsMarks=PhysicsMarks,ChemistryMarks=ChemistryMarks,CsMarks=CsMarks)
            StudentObj.save()
            return redirect('display')
        except Exception as e:
            print(e)    
        

    return render(request,'Form.html')


#method to display all data of student
def display(request):
    #make a list to store the all percentage of all students
    List=[]
    #fetch the all data from studentData
    studentData=StudentMarks.objects.all()
    
    #surround with try and except
    #store percentage of all students into a list
    try:
        for eachstudent in studentData:
            percentage=eachstudent.get_percentage()
            List.append(percentage)
     
    except Exception as e:
        print(e) 
        
    #make a context dict 
    #pass List and students data into marks.html file    
     
    context={'List':List,'studentData':studentData} 
    return render(request,'marks.html',context)    
      
    
    
   
   
   
   
   
   
   
   
   
   
   
   
 
 
 
