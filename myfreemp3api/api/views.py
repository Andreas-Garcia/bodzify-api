from django.contrib.auth.models import User, Group
from myfreemp3api.api.models import *
from rest_framework import viewsets
from .serializers import *
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from myfreemp3api.myfreemp3_scrapper import scrapper
import myfreemp3api.api.configuration as api_cfg

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

@csrf_exempt
def UserCreationView(request):
    if (request.method == "POST"):
        return HttpResponseRedirect("lol")
    
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

def SongView(request):
    if (request.method == "GET"):
        queryParameterName = api_cfg.configuration["queryParameterName"]
        return JsonResponse(scrapper.scrap(request.GET.get(queryParameterName, '')), safe=False)