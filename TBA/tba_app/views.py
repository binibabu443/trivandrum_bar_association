from django.shortcuts import render
from tba_app.models import registration,admin,contact
from django.http import HttpResponse
from datetime import date,timedelta,datetime

# Create your views here.
def register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        types=request.POST.get('types')
        officeadd=request.POST.get('officeadd')
        residenceadd=request.POST.get('residenceadd')
        joiningdate=request.POST.get('joiningdate')
        duration=request.POST.get('duration')
        password=request.POST.get('cnfrmpassword')
        a=registration(name=name,mobileno=mobile,emailid=email,types=types,officeadd=officeadd,residenceadd=residenceadd,joiningdate=joiningdate,duration=duration,status='Pending',password=password)
        a.save()
        return render(request,'registration.html')

def viewreg(request):
    queryset=registration.objects.all()
    return render(request,'adminhome.html',{'authors':queryset})

def view_approved_reg(request):
    queryset=registration.objects.all().filter(status='Approved')
    return render(request,'index.html',{'authors':queryset})

def view_pending_reg(request):
    queryset=registration.objects.all().filter(status='Pending')
    return render(request,'viewregistration.html',{'authors':queryset})

def approval(request):
    if request.method=='POST':
        id=request.POST.get('id')
        q=registration.objects.all().filter(id=id)[0]
        dur=q.duration
        join=q.joiningdate
        if dur=='3 months':
            dd=90
        elif dur=='6 months':
            dd=180
        elif dur=='1 Year':
            dd=365
        elif dur=='5 Years':
            dd=1825
        d=timedelta(dd)
        exp=join+d
        today = str(date.today())
        registration.objects.filter(id=id).update(status='Approved',approvedate=today,expirydate=exp)
        return view_pending_reg(request)

def authenticate(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        u=admin.objects.all().filter(emailid=email,password=password)
        if u.count()==1:
            return render(request,'adminhome.html')
        else:
            u=registration.objects.all().filter(emailid=email,password=password,status='Approved')
            request.session['email']=email
            if u.count()==1:
                return render(request,'memberhome.html')
            else:
                return HttpResponse('Login Failed')

def submitmsg(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        a=contact(name=name,emailid=email,subject=subject,msg=message,status='off')
        a.save()
        return render(request,'index.html')

def viewmsg(request):
    queryset=contact.objects.all().filter(status='off')
    return render(request,'contacts.html',{'authors':queryset})

def readmsg(request):
    if request.method=='POST':
        id=request.POST.get('id')
        contact.objects.filter(id=id).update(status='on')
        return viewmsg(request)

def viewprofile(request):
    queryset=registration.objects.filter(emailid=request.session['email'])
    return render(request,'profileview.html',{'author':queryset})

def editprofileview(request):
    queryset=registration.objects.filter(emailid=request.session['email'])
    return render(request,'editprofile.html',{'author':queryset})

def editprofile(request):
    if request.method=='POST':
        ide=request.POST['id']
        name=request.POST['name']
        mobile=request.POST['mobile']
        email=request.POST['email']
        types=request.POST['types']
        officeadd=request.POST['officeadd']
        residenceadd=request.POST['residenceadd']
        password=request.POST['password']
        
        registration.objects.filter(id=ide).update(name=name,mobileno=mobile,emailid=email,types=types,officeadd=officeadd,residenceadd=residenceadd,password=password)
        return viewprofile(request)

def expiry(request):
    query=registration.objects.all()
    dictnry={}
    for i in query:
        dictnry[query.expirydate]=query.id
    for i in dictnry.keys():
        if i<=str(date.today()):
            registration.objects.filter(id=dictnry[i]).update(status='Expired')

