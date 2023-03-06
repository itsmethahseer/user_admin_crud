from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import never_cache

from .forms import user_form


# Create your views here.
@never_cache
def Logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')

@never_cache
def sign(request):
    if request.user.is_authenticated:
        return render(request, 'user_home.html')
    if request.method=='POST':
        uname =request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if uname and email and pass2 and pass1 is None:
            return HttpResponse("please fill properly")
        if pass1!=pass2:
            return HttpResponse("Your password and conform password are not same")
        else:
            my_user =User.objects.create_user(uname,email,pass1)
            my_user.save()
        #return HttpResponse("User has been created successfully")
            return redirect('login')
            #print(uname,email,pass1,pass2)

    return render(request, 'sign.html')

@never_cache
def login_page(request):
    if request.user.is_authenticated:
        return redirect('user_home')
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            # request.session['username'] = username

            login(request,user)
            return redirect('user_home')
        else:
            return HttpResponse("username or password is incorrect")
    return render(request, 'login.html')
@never_cache
def Homepage(request):
    if request.user.is_authenticated:
        return render(request, 'user_home.html')
    else:
        return redirect(login_page)


@never_cache
def adminlogin(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('adminpage')

    if request.method=='POST':
        print('reached adminpage')
        username=request.POST['username']
        password=request.POST['pass']
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_superuser:
                login(request,user)
                print('reached adminpage')
                return redirect('adminpage')
        else:
            return render(request,'admin.html',{'invalid':"Invalid Credentials"})
    else:
         return render(request,'admin.html')


@never_cache
def adminpage(request):
    if request.user.is_authenticated and request.user.is_superuser:
# Here i collects the full datas from(users detais) database to the dictionary user_list
        new=User.objects.all()
        context = {'user_list':new}
        return render(request,'admin_home.html',context)
    return redirect(adminlogin)

@never_cache
def admin_logout(request):
    logout(request)
    return redirect('adminlogin')
# for updating the username,passwords
def user_insert(request,id):
    user=User.objects.get(id=id)
    form=user_form(instance=user)
    if request.method == 'POST' :
        form=user_form(request.POST, instance=user)
        print('>>>>>>>>>>>>>>')
        if form.is_valid():
           print('}}}}}}}}}}}}}}}}}}}}}}')
           form.save()
           return redirect('adminpage')

    return render(request,'admincreation.html',{'form':form})
@login_required(login_url='adminlogin')
def admin_delete(request, id):
    User.objects.get(id=id).delete()
    return redirect('adminpage')


def add_user(request):
    print('helo')
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        # if password == confirm:
        if User.objects.filter(username=username).exists():

            return render(request, 'adduser.html', {'error_msg': "username already taken"})
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            print('user created')
            return redirect('adminpage')
    # else:
    # print("wrong password")
    # return render(request,'adduser.html',{'pass_msg':"wrong password"})
    else:

        return render(request, 'adduser.html')

    # return render(request,'adduser.html')


@login_required(login_url='adminlogin')
def search(request):
    if request.method == 'GET':
        print("search")
        query = request.GET.get('query')
        if query:
            print("admin")
            user = User.objects.filter(username__icontains=query)
            context = {'user_list': user}
            return render(request, 'adminsearch.html', context)


        else:
            print("no data")
            return render(request, 'adminpage.html')






