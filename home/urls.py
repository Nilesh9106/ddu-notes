from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.homeView,name='home'),
    path('upload/', views.uploadView,name='upload'),
    path('login/', views.loginView,name='login'),
    path('change-pic/', views.changePicView,name='changePic'),
    path('signup/', views.signupView,name='signup'),
    path('logout/', views.logoutView,name='logout'),
    path('college-notes/', views.collegeView,name='collegeNotes'),
    path('profile/', views.profileView,name='profile'),
    path('<str:user>/', views.userNoteView,name='userNote'),

]
