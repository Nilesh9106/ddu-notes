from django.shortcuts import render,redirect
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from home.forms import *
from django.contrib import messages
from django.db.models import Q
# Create your views here.

def homeView(request):
    if request.GET.get('searchfield') is not None:
        search = request.GET.get('searchfield')
        result1=Note.objects.filter(title__icontains=search,visibility='3')
        result2=Note.objects.filter(subject__icontains=search,visibility='3')
        result3=Note.objects.filter(description__icontains=search,visibility='3')
        notes = result1.union(result2).union(result3)
    else:
        notes = Note.objects.filter(visibility = '3')
    
    return render(request,'home/home.html',{'notes':notes})

def loginView(request):
    if request.user.is_authenticated == True :
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}.")
                return redirect('home')
    form=AuthenticationForm()

    return render(request,'auth/login.html',{'form':form})

def signupView(request):
    if(request.user.is_authenticated == True):
        return redirect('home')
    if request.method == 'POST':
        form = Signup(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                messages.error(request,'This email is In Already use try Another !!')    
                return redirect('signup')
            user=form.save()
            
            
            
            domain = email[(email.index('@')+1):]
            print(domain)
            if College.objects.filter(domain=domain).exists():
                college=College.objects.filter(domain=domain).first()
                profile=UserProfile(user=user,college=college)
            else:
                profile=UserProfile(user=user)
            
            profile.save()

            return redirect('login')
        
    form=Signup()
    
    return render(request,'auth/signup.html',{'form':form})

def logoutView(request):
    if(request.user.is_authenticated == False):
        return redirect('login')
    logout(request)
    return redirect('login')

def uploadView(request):
    if(request.user.is_authenticated == False):
        return redirect('login')
    
    if request.method == 'POST':
        form=UploadForm(request.POST,request.FILES)
        if form.is_valid():
            
            note=form.save(commit=False)
            profile = UserProfile.objects.filter(user=request.user).first()
            if profile.college == None:
                messages.error(request,'please add your college email id in profile section!!')
                return redirect('home')
            
            note.user = profile
            note.save()
            return redirect('/'+request.user.username)
    else:
        form = UploadForm()
    
    return render(request,'notes/upload.html',{'form':form})

def profileView(request):
    if(request.user.is_authenticated == False):
        return redirect('login')
    
    profile = UserProfile.objects.filter(user=request.user).first()
    notes = Note.objects.filter(user=profile).count()
    if request.method == 'POST':
        form = UserForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    form = UserForm(instance=request.user)
    form2 = ProfilePicForm(instance=profile)
    return render(request,'home/profile.html',{'profile':profile,'count':notes,'form':form,'form2':form2})


def userNoteView(request,user):
    if User.objects.filter(username=user).exists():
        user= User.objects.filter(username=user).first()
        profile = UserProfile.objects.filter(user=user).first()
        if request.user.is_authenticated and request.user.username == user.username :
            notes = Note.objects.filter(user=profile)
        else:
            notes = Note.objects.filter(user=profile,visibility='3')
        return render(request,'notes/userNotes.html',{'notes':notes})
    else:
        return redirect('home')

def changePicView(request):
    if request.method == 'POST':
        profile = UserProfile.objects.filter(user=request.user).first()
        form = ProfilePicForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return redirect('home')



def collegeView(request):
    if(request.user.is_authenticated == False):
        return redirect('login')
    
    user = request.user
    profile= UserProfile.objects.filter(user=user).first()
    college = profile.college
    notes = []
    for user in UserProfile.objects.filter(college=college):
        note = Note.objects.filter(user=user,visibility='2' )
        notes = notes + list(note)
    return render(request,'notes/collegeNotes.html',{'notes':notes,'college':college})
    

def searchView(request):
    search = request.GET.get('searchfield')
    result1=Note.objects.filter(title__icontains=search,visibility='3')
    result2=Note.objects.filter(subject__icontains=search,visibility='3')
    result3=Note.objects.filter(description__icontains=search,visibility='3')

    result = result1.union(result2).union(result3)
    
    return render(request,'notes/searchResult.html',{'notes':result})