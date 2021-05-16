from django.http import HttpResponse
from django.shortcuts import render
from .models import place

# Create your views here.
# def demo(request):
#     return HttpResponse("hai avodha")
def demo(request):
    obj = place.objects.all()

    obj.name='kerala'
    obj.desc='This is kerala'
    obj.price=100

    return render(request, "index.html", {'results': obj})


