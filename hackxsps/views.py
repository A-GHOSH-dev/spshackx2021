from django.http.response import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from hackxsps.models import Registration
from django.urls import reverse



# Create your views here.
def index(request):
    #return HttpResponse("This is my home page")
    return render(request, 'index.html')
def submitted(request):
        #return HttpResponse("This is my contacts page")
    return render(request, 'submitted.html')

def registration(request):
    regstudentdata = Registration.objects.all()
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']        
        email=request.POST['email']
        
        phone=request.POST['phone']
        
        
        
        college=request.POST['college']
        year=request.POST['year']
        stream=request.POST['stream']
        track=request.POST['track']
        teamnum=request.POST['teamnum']
        teamname=request.POST['teamname']
        teammemname1=request.POST['teammemname1']
        teammememail1=request.POST['teammememail1']
        teammemname2=request.POST['teammemname2']
        teammememail2=request.POST['teammememail2']
        teammemname3=request.POST['teammemname3']
        teammememail3=request.POST['teammememail3']
        teammemname4=request.POST['teammemname3']
        teammememail4=request.POST['teammememail3']
        


        studentdata = Registration(firstname=firstname, lastname=lastname, email=email, phone=phone, college=college, year=year, stream=stream,track=track, teamnum=teamnum, teamname=teamname, teammemname1=teammemname1, teammememail1=teammememail1, teammemname2=teammemname2, teammememail2=teammememail2, teammemname3=teammemname3, teammememail3=teammememail3,teammemname4=teammemname4, teammememail4=teammememail4)  

        studentdata.save()
        res = "Dear {} Thanks for your registration".format(firstname)
        #return render(request,"registration.html",{"status":res,"Registered":regstudentdata})
        return HttpResponseRedirect(reverse('submitted.html'))
        
    else:
        #return HttpResponse(request,"registration.html",{"Registered":regstudentdata})
        return HttpResponse('Invalid Response')









"""
        print(firstname, lastname, email, phone, college, year, stream, domain, teamnum, teamname, teammemname1,teammememail1, teammemname2, teammememail2, teammemname3, teammememail3,teammemname4,teammememail4)

        ins = Registration(firstname=firstname, lastname=lastname, email=email, phone=phone, college=college, year=year, stream=stream,domain=domain, teamnum=teamnum, teamname=teamname, teammemname1=teammemname1, teammememail1=teammememail1, teammemname2=teammemname2, teammememail2=teammememail2, teammemname3=teammemname3, teammememail3=teammememail3,teammemname4=teammemname4, teammememail4=teammememail4)  

        ins.save()
        print("Data stored in db")"""
        
   

def submission(request):
    #return HttpResponse("This is my projects page")
    return render(request, 'submission.html')
def checkin(request):
    #return HttpResponse("This is my contacts page")
    return render(request, 'checkin.html')

def projects(request):
        #return HttpResponse("This is my contacts page")
    return render(request, 'projects.html')

def submitted(request):
        #return HttpResponse("This is my contacts page")
    return render(request, 'submitted.html')



def table(request):
    regstudentdata = Registration.objects.all()
    
    return render(request,"table.html",{"regstudentdata":regstudentdata})