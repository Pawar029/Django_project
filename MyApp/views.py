from django.http import HttpResponse
from django.shortcuts import render
from MyApp.models import Event
# Create your views here.

def index(request):
     
    return render(request,'index.html')
    # return HttpResponse("This is my first page")
 

def home(request):
    return render(request,'home.html')
def events(request):
    if request.method == "POST":
        game = request.POST.get('game')
        date = request.POST.get('date')
        time = request.POST.get('time')

        # temp = Event()
        # temp.game = game
        # temp.date = date
        # temp.time = time
        temp = Event(game=game,date=date,time=time)
        temp.save()

    #to view database in the form of table
    from django.core import serializers
    data = serializers.serialize("python",Event.objects.all())
    
    context = {
        "data" : data,
    
    }

    return render(request,'events.html',context)

def vargani(request):
    return render(request,'vargani.html')

