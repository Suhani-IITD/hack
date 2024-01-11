from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.new, name='new'),
    path('login', views.login, name='login'),
    path('SignUp',views.create, name = 'SignUp'),
    path('interface',views.interface, name = 'interface'),
    path('appointments',views.appoint, name = "appointments"),
    path('dashboard',views.dash, name = 'dashboard'),
    #path('voice', views.handle_voice_input, name = 'voice')

]
