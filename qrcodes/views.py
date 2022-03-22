from django.shortcuts import render
from django.http import HttpResponse
import qrcode


from .models import Flange



def index(request):
    return render(request, 'qrcodes/index.html')

def save_flange(request):
    img = qrcode.make(f"https://smartmaintain.herokuapp.com/qrcodes/get_torque/{request.POST['aks-number']}/{request.POST['flange-number']}")
    img.save(f"media/{request.POST['aks-number']}_{request.POST['flange-number']}.png")
    f = Flange(
        flange_number = int(request.POST['flange-number']),
        torque = int(request.POST['torque']),
        aks_number = request.POST['aks-number'],
    )
    f.save()
    
    return HttpResponse('save was successful')

def get_torque(request, aks_number, flange_number):
    flange = Flange.objects.get(flange_number=flange_number)
    torque = flange.torque
    return HttpResponse(f"Der Flansch Nr. {flange_number} von {aks_number} ist mit {torque} Nm anzuziehen.")