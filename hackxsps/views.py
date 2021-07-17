from django.shortcuts import render, HttpResponse
from hackxsps.models import Registration

# Create your views here.
def index(request):
    #return HttpResponse("This is my home page")
    return render(request, 'index.html')

def registration(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']        
        email=request.POST['email']
        country=request.POST['country']
        state=request.POST['state']
        city=request.POST['city']
        address=request.POST['address']
        pin=request.POST['pin']
        phone=request.POST['phone']
        
        whatsapp=request.POST['whatsapp']
        
        college=request.POST['college']
        year=request.POST['year']
        stream=request.POST['stream']
        team=request.POST['team']
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
        

        print(firstname, lastname, email, country, state, city, address, pin, phone, whatsapp, college, year, stream, team, teamnum, teamname, teammemname1,teammememail1, teammemname2, teammememail2, teammemname3, teammememail3,teammemname4,teammememail4)

        ins = Registration(firstname=firstname, lastname=lastname, email=email, country=country, state=state, city=city, address=address, pin=pin, phone=phone, whatsapp=whatsapp, college=college, year=year, stream=stream, team=team, teamnum=teamnum, teamname=teamname, teammemname1=teammemname1, teammememail1=teammememail1, teammemname2=teammemname2, teammememail2=teammememail2, teammemname3=teammemname3, teammememail3=teammememail3,teammemname4=teammemname4, teammememail4=teammememail4)  

        ins.save()
        print("Data stored in db")
        
    #return HttpResponse("This is my blogs page")
    return render(request, 'registration.html')


def submission(request):
    #return HttpResponse("This is my projects page")
    return render(request, 'submission.html')
def checkin(request):
    #return HttpResponse("This is my contacts page")
    return render(request, 'checkin.html')

def projects(request):
        #return HttpResponse("This is my contacts page")
    return render(request, 'projects.html')



