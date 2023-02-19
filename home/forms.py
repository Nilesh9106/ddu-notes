from django import forms 
from home.models import *
from django.contrib.auth.forms import UserCreationForm
class NoteForm(forms.ModelForm):
    class Meta:
        model=Note
        fields ='__all__'

class Signup(UserCreationForm):
    class Meta:
        model=User
        fields= ['username', 'first_name','last_name','email', 'password1', 'password2']
        widgets={
            'email':forms.EmailInput(attrs={
                'required':True
            })
        }

class UploadForm(forms.ModelForm):

    class Meta:
        model=Note
        fields=['subject','semester','department','title','document']

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email']



        