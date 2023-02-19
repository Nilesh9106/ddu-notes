from django.shortcuts import render,redirect
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from home.forms import *
from django.contrib import messages
from django.db.models import Q
# Create your views here.
from .filters import NoteFilter
from verify_email.email_handler import send_verification_email

def homeView(request):
    if(request.user.is_authenticated == False):
        return redirect('login')
    notes = Note.objects.all()
    myFilter = NoteFilter(request.GET, queryset=notes)
    notes = myFilter.qs
    
    
    return render(request,'home/home.html',{'notes':notes,'myfilter':myFilter})

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
            domain = email[(email.index('@')+1):]
            if domain == 'ddu.ac.in':
                inactive_user = send_verification_email(request, form)
                messages.success(request,'Check Your Email for Verification')
                return redirect('signup')
            else:
                messages.error(request,'Please Enter DDU email id ')
        
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
            note.user = request.user
            note.save()
            return redirect('/'+request.user.username)
    else:
        form = UploadForm()
    
    return render(request,'notes/upload.html',{'form':form})

def profileView(request):
    if(request.user.is_authenticated == False):
        return redirect('login')
    
    
    notes = Note.objects.filter(user=request.user).count()
    if request.method == 'POST':
        form = UserForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    form = UserForm(instance=request.user)
    return render(request,'home/profile.html',{'count':notes,'form':form})


def userNoteView(request,user):
    if User.objects.filter(username=user).exists():
        user= User.objects.filter(username=user).first()
        notes = Note.objects.filter(user=user)
        return render(request,'notes/userNotes.html',{'notes':notes})
    else:
        return redirect('home')

    



def deleteNoteView(request,id):
    user = request.user
    if(request.user.is_authenticated == False):
        return redirect('login')
    if Note.objects.filter(id=id,user=user).exists():
        note = Note.objects.filter(id=id,user=user).first()
        
        note.delete()
    return redirect('userNote',user)

