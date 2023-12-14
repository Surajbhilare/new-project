from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User

def index(request):
    template = loader.get_template("index.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))


def java(request):
    template = loader.get_template("java.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))

def online(request):
    template = loader.get_template("online.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))

def company(request):
    template = loader.get_template("company.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))


def login(request):
    template = loader.get_template("login.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))


def register(request):
    template = loader.get_template("register.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))

def enterprises(request):
    template = loader.get_template("enterprises.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))


def training(request):
    template = loader.get_template("training.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))


def terms(request):
    template = loader.get_template("terms.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))


