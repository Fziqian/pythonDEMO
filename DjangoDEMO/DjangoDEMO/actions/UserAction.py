import json
from django.http import HttpResponse

from DjangoDEMO.actions.RetWrapper import *
from DjangoDEMO.business import UserBis

def getUserByName(request):
    data=UserBis.getUserByName()
    ret=RetWrapper(Data=data)
    return HttpResponse(ret.toJSON())