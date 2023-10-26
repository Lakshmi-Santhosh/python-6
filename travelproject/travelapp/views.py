from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Person


# Create your views here.
def demo(request):
    obj=Place.objects.all()
    sub=Person.objects.all()
    return render(request,"index.html",{'result':obj,'result1':sub})