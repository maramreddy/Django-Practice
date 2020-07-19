from django.shortcuts import render
from django.http import HttpResponse
from .models import Person, Amount
# Create your views here.
from .forms import NewUserForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def debts_home(request):
    # return HttpResponse("<h1> welcome to my debts home </h1>")
    debts_context = {'name':'papi reddy'}
    return render(request,'debts/home.html',context=debts_context)

def debts_persons(request):
    persons = Person.objects.all()
    persons_data = {'persons': persons}
    return render(request,'debts/person.html',context=persons_data)

def register_debts(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return debts_home(request)
        else:
            print("ERROR: Invalid Form")

    return render(request,'debts/register_debts.html',context={'form':form})

def register(request):
    registered = False
    userForm = UserForm()
    userProfileForm = UserProfileForm()
    if request.method == 'POST':
        userForm = UserForm(data=request.POST)
        userProfileForm = UserProfileForm(data=request.POST)
        if userForm.is_valid() and userProfileForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            profile = userProfileForm.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(userForm.errors,userProfileForm.errors)
    return render(request,'debts/register.html',context={'user_form':userForm,
                                                         'profile_form':userProfileForm,
                                                         'registered': registered
                                                         })

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return render(request,'index.html')
        else:
            messages.info(request,"invalid login credentials supplied")
            return render(request,'debts/login.html')
    else:
        return render(request,'debts/login.html')

def user_logout(request):
    logout(request)
    return render(request,'index.html',{})