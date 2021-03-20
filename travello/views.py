from django.shortcuts import render
from.models import Mini_pohled
from.models import Destination

# Create your views here.

def index(request):

    #manuální část
    sekce = Mini_pohled()
    sekce.title = "Top destinations"
    sekce.title_low = "Beach, Ocean, 5-star Hotel"
    sekce.img = 'beach.svg'

    sekce2 = Mini_pohled()
    sekce2.title = "Best prices"
    sekce2.title_low = "All inclusive"
    sekce2.img = 'wallet.svg'

    sekce3 = Mini_pohled()
    sekce3.title = "Term"
    sekce3.title_low = "2-4, 4-7, 7-10"
    sekce3.img = 'suitcase.svg'

    sections = [sekce, sekce2, sekce3]
    
    #pgAdmin část

    dests = Destination.objects.all()

    return render(request,"index.html",{"sections": sections,"dests":dests})

