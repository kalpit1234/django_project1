from django.shortcuts import render ,redirect
from.models import*
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
@login_required(login_url='/login_page')
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
    from django.db.models import Q
    if request.GET.get('search'):
        
        queryset=queryset.filter(reciepe_name__icontains=request.GET.get('search'))   
    return render(request,"reciepe.html",context) 
@login_required(login_url='/login_page')
def Delete_recieps(request,id):
    queryset=Reciepe.objects.get(id=id)
    
    queryset.delete()
    return redirect('/recieps/')
@login_required(login_url='/login_page')
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
    return render(request,"update_recieps.html",context)        
def login_page(request):
    if request.method=="POST": 
        data=request.POST
        username=data.get("username")
        password=data.get('password')
        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid username')
            return redirect('/login_page/')
        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request,'Invalid password')
            return redirect('/login_page/')
        else:
            login(request,user)
            return redirect('/recieps/')
    return render(request,"login.html")  
def logout_page(request):
    logout(request)
    return redirect('/login_page/')       

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
            return redirect('/register_page/')
        
        user=User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save()
        messages.info(request,'account succesfully run')
    return render(request,"register.html")
def like(request):
    return render(request,'like.html')
from django.db.models import Q,Sum
def get_students(request):
    queryset=Student.objects.all()
    if request.GET.get('search'):
        search= request.GET.get('search')
        queryset=queryset.filter(
            Q(student_name__icontains=search)|
            Q(department__department__icontains=search)|
              Q(student_id__student_id__icontains=search)|
               Q(student_email__icontains=search)|
                 Q(student_age__icontains=search)
               
               
        )
            
                
    paginator = Paginator(queryset, 25 )  # Show 25 contacts per page.

    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    print(page_obj.count)
    return render(request, "report/students.html", {"queryset": page_obj})
    




  
from.seed import generate_report_card    
def see_marks(request,student_id):
    generate_report_card
    queryset=Subjectmarks.objects.filter(student__student_id__student_id=student_id)
    total_marks=queryset.aggregate(total_marks=Sum('marks'))
    current_rank=-1
    ranks=Student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks','-student_age')
    i=1
    for rank in ranks:
        print(rank.student_id)
        if student_id==rank.student_id.student_id:
            current_rank = i
            break
        i=i+1
    return render(request,"report/see_marks.html",{"queryset":queryset,"total_marks":total_marks,"current_rank":current_rank})
    