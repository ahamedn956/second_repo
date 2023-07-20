from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def start(request):
    return HttpResponse('<h2>hello world..........</h2>')
def end(request):
    return HttpResponse('<h3><marquee><i>Come on lets give a Smile.............</i></marquee></h3>')
