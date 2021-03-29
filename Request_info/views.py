from django.shortcuts import render
from .models import Request_info
# Create your views here.

def Requestinfo(request):
    Email_address=request.POST['Email_address']
    Name=request.POST['Name']
    Subject=request.POST['Subject']
    Question=request.POST['Question']
    Save_requestinfo=Request_info(Email_address=Email_address,Name=Name,Subject=Subject,Question=Question)
    Save_requestinfo.save()
    return render(request,'index.html')