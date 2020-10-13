from django.shortcuts import render

def index(response):
    return render (response, "main/home.html")

def home(response):
    return render (response, "templates/main/home.html")