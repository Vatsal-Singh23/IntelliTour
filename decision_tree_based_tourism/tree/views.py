from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from .models import *



def index(request):
    return render(request,'index.html')

def login(request):
    error=""
    if request.method == "POST":
        ur = request.POST['uname']
        pd = request.POST['pwd']
        user = auth.authenticate(username=ur,password=pd)
        try:
            if user.is_staff:
                auth.login(request,user)
                error = "no"
            elif user is not None:
                person = Signup.objects.get(user=user)
                if person.status == "Confirm":
                    auth.login(request,user)
                    error = "not"
                elif person.status == "Pending":
                    error='wait'
                else:
                    error="out"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error':error,'error':error}
    return render(request,'login.html',d)

def signup(request):
    error = ""
    if request.method=='POST':
        f=request.POST['fname']
        l=request.POST['lname']
        e = request.POST['email']
        con = request.POST['contact']
        p = request.POST['pwd']
        gen = request.POST['gender']
        i=request.FILES['image']
        addr=request.POST['address']
        d=request.POST['dob']
        try:
            user=User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
            Signup.objects.create(user=user,mobile=con,image=i,gender=gen,address=addr,dob=d,status="Confirm")
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'signup.html',d)

def admin_home(request):
    return render(request,'admin_home.html')

def user_home(request):
    data = Signup.objects.get(user=request.user)
    d = {'data':data}
    return render(request,'user_home.html',d)

def logout(request):
    auth.logout(request)
    return redirect('/')

def users(request):
    data = Signup.objects.all()
    data = data[::-1]
    d = {'data':data}
    return render(request,'users.html',d)

def delete_user(request,id):
    student = User.objects.get(id=id)
    student.delete()
    return redirect('users')


def edit_profile(request):
    error=""
    data=User.objects.get(id=request.user.id)
    data2=Signup.objects.get(user=request.user)
    if request.method=='POST':
        f = request.POST['fname']
        l = request.POST['lname']
        c = request.POST['contact']
        g = request.POST['gender']
        do = request.POST['dob']
        data.first_name=f
        data.last_name=l
        data2.mobile=c
        data2.gender=g
        data2.dob=do
        try:
            data.save()
            data2.save()
            error="no"
        except:
            error="yes"
        try:
            i=request.FILES['profilepic']
            data2.image=i
            data2.save()
            error="no"
        except:
            pass
    d={'data':data,'data2':data2,'error':error}
    return render(request,'edit_profile.html',d)


def add_package(request):
    print('>>>')
    error=""
    i2=0
    i3=0
    if request.method=='POST':
        n = request.POST['pname']
        p = request.POST['price']
        c = request.POST['city']
        du = request.POST['duration']
        i1 = request.FILES['packimg']
        de = request.POST['desc']
        pt = request.POST['packageType']
        try:
            i2 = request.FILES['packimgg']
        except:
            pass
        try:
            i3 = request.FILES['packimggg']
        except:
            pass
        try:
            if(i2 == 0 and i3 == 0):
                Package.objects.create(name=n,image1=i1,description=de,price=p,duration=du,city=c,packageType=pt)
            elif(i3==0):
                Package.objects.create(name=n,image1=i1,image2=i2,description=de,price=p,duration=du,city=c,packageType=pt)
            else:
                Package.objects.create(name=n,image1=i1,image2=i2,image3=i3,description=de,price=p,duration=du,city=c,packageType=pt)
            error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'add_package.html',d)


def manage_package(request):
    data = Package.objects.all()
    d = {'data':data}
    return render(request,'manage_package.html',d)


def delete_package(request,id):
    data=Package.objects.get(id=id)
    data.delete()
    return redirect('manage_package')


def edit_package(request,id):
    error=""
    data=Package.objects.get(id=id)
    if(not data.image2):
        data.image2=0
    if(not data.image3):
        data.image3=0
    if request.method=='POST':
        n = request.POST['pname']
        p = request.POST['price']
        c = request.POST['city']
        du = request.POST['duration']
        de = request.POST['desc']
        pt = request.POST['packageType']
        try:
            i1 = request.FILES['packimg']
            data.image1=i1
        except:
            pass
        try:
            i2 = request.FILES['packimgg']
            data.image2=i2
        except:
            pass
        try:
            i3 = request.FILES['packimggg']
            data.image3=i3
        except:
            pass
        data.name=n
        data.price=p
        data.city=c
        data.duration=du
        data.description=de
        data.packageType=pt
        try:
            data.save()
            error="no"
        except:
            error="yes"
        de = request.POST['desc']
    d = {'data':data,'error':error}
    return render(request,'edit_package.html',d)


def view_packages(request):
    data = Package.objects.all()
    d = {'data':data}
    return render(request,'view_packages.html',d)


def book_package(request,id):
    error=""
    error2=""
    data = Package.objects.get(id=id)
    if(not data.image2):
        data.image2=0
    if(not data.image3):
        data.image3=0

    # Adding Review
    review = Review.objects.filter(packageID=id)
    if request.method == 'POST':
        if 'star' in request.POST and 'review' in request.POST:
            s=request.POST['star']
            r=request.POST['review']
            try:
                Review.objects.create(packageID=id,packagename=data.name,userName=request.user.first_name,review=r,rating=s)
                error="no"
            except:
                error="yes"
        else:
            data2=Signup.objects.get(user=request.user)
            c=request.POST['count']
            date=request.POST['tdate']
            t=request.POST['type']
            c=request.POST['city']
            ta=request.POST['totalamount']
            name = request.user.first_name+' '+request.user.last_name
            email = request.user.username
            mobile = data2.mobile
            try:
                Booking.objects.create(name=name,email=email,number=mobile,packageID=id,packagename=data.name,count=c,date=date,
                                       type=t,city=c,amount=ta,status="Pending")
                error2="no"
            except:
                error2="yes"

    d = {'data':data,'error':error,'review':review,'error2':error2}
    return render(request,'book_package.html',d)


def my_booking(request):
    data = Booking.objects.all()
    d = {'data':data}
    return render(request,'my_booking.html',d)


def view_booking(request):
    error=""
    data = Booking.objects.all()
    if request.method=='POST':
        pid = request.POST['pid']
        s = request.POST['status']
        print(pid,s)
        data2 = Booking.objects.get(id=pid)
        data2.status=s
        try:
            data2.save()
            error="no"
        except:
            error="yes"
    d = {'data':data,'error':error}
    return render(request,'view_booking.html',d)


def search(request):
    n=request.POST['name']
    data = Package.objects.filter(packageType__icontains=n)
    d={'data':data}
    return render(request,'view_packages.html',d)


def search2(request):
    data=[]
    n=int(request.POST['price'])
    data = Package.objects.filter(price__lte=n)
    # data2 = Package.objects.all()
    # data = [num for num in data2 if num.price <= n]
    # print('value of n =',data)

    d={'data':data}
    return render(request,'view_packages.html',d)


