from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.new, name='new'),
    path('login', views.login, name='login'),
    path('SignUp',views.create, name = 'create'),
    path('interface',views.interface, name = 'interface')

]
