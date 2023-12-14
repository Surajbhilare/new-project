from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('java', views.java, name='java'),
    path('online', views.online, name='online'),
    path('company', views.company, name='company'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('enterprises', views.enterprises, name='enterprises'),
    path('training', views.training, name='training'),
    path('terms', views.terms, name='terms'),
     
]