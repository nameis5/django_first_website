from django.http import HttpResponse
from django.shortcuts import render
  
def index(request):
    return render(request, "beta_main.html")

def straight(request):
    return render(request, "straight.html")

def triangle(request):
    return render(request, "triangle.html")

def quadrilateral(request):
    return render(request, "quadrilateral.html")

def area(request):
    return render(request, "area.html")

def circle(request):
    return render(request, "circle.html")

def trigonometry(request):
    return render(request, "trigonometry.html")
