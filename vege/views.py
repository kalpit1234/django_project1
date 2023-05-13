from django.shortcuts import render ,redirect
from.models import*
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
@login_required(login_url='/login')
def recieps(request):
    if request.method == "POST":
        data = request.POST
        
        reciepe_name=data.get("reciepe_name")
        reciepe_description=data.get("reciepe_description")
        reciepe_image=request.FILES.get("reciepe_image")
        reciepe_comment=data.get("reciepe_comment")
        Reciepe.objects.create(
            reciepe_name=reciepe_name,
            reciepe_description=reciepe_description,
            reciepe_image=reciepe_image,
            reciepe_comment=reciepe_comment,
        )
        return redirect("/recieps/")
    querset=Reciepe.objects.all()
    context={"recieps":querset}
    if request.GET.get('search'):
        queryset=queryset.filter(reciepe_name__icontains=request.GET.get('search'))
        

                 
            

            
            
        
        
            
    return render(request,"reciepe.html",context)    
@login_required(login_url='/login')
def Delete_recieps(request,id):
    queryset=Reciepe.objects.get(id=id)
    
    queryset.delete()
    return redirect('/recieps/')
@login_required(login_url='/login')
def update_recieps(request,id):
    queryset=Reciepe.objects.get(id=id)
    if request.method =="POST":
        data=request.POST
        reciepe_name=data.get("reciepe_name")
        reciepe_description=data.get("reciepe_description")
        reciepe_image=request.FILES.get("reciepe_image")
        queryset.reciepe_name=reciepe_name
        queryset.reciepe_description=reciepe_description
        if reciepe_image:
            queryset.reciepe_image=reciepe_image
        queryset.save()
        return redirect('/recieps/')
    context={"reciepe":queryset}
    return render(request,"update_recieps.html")        
def login_page(request):
    if request.method=="POST": 
        data=request.POST
        username=data.get("username")
        password=data.get('password')
        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid username')
            return redirect('/login/')
        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request,'Invalid password')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/recieps/')
    return render(request,"login.html")  
def logout_page(request):
    logout(request)
    return redirect('/login/')       

def register_page(request):
    if request.method=="POST": 
        data=request.POST
        username=data.get("username")
        first_name=data.get("first_name")
        last_name=data.get('last_name')
        password=data.get('password')
        user=User.objects.filter(username=username)
        
        if user.exists():
            messages.error(request,'username already taken')
            return redirect('/register/')
        
        user=User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save()
        messages.info(request,'account succesfully run')
    return render(request,"register.html")
    
    
    
    

    