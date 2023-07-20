from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def str1(request):
    return HttpResponse('<h1><i>Hii this my Naruto story</h1>')
def str2(request):
    return HttpResponse('<h2><marquee><i>Lets fight together.....lets go.....</i></marquee></h2>')