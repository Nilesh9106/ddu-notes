from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView,name='home'),
    path('upload/', views.uploadView,name='upload'),
    path('login/', views.loginView,name='login'),
    path('signup/', views.signupView,name='signup'),
    path('logout/', views.logoutView,name='logout'),
    path('profile/', views.profileView,name='profile'),
    path('<str:user>/', views.userNoteView,name='userNote'),
    path('delete/<int:id>', views.deleteNoteView,name='delete'),

]
