from django.shortcuts import render
from django.views import View
from.models import Rainbow
from django.http import HttpResponse
# Create your views here.
class RainbowInput(View):
    def get(self,request):
        return render(request,'rainbowinput.html')
class RainbowInsert(View):
    def get(self,request):
        p_id=int(request.GET["t1"])
        p_name=request.GET["t2"]
        p_cost=float(request.GET["t3"])
        p_mfdt=request.GET["t4"]
        p_expdt=request.GET["t5"]
        p1=Rainbow(pid=p_id,pname=p_name,pcost=p_cost,pmfdt=p_mfdt,pexpdt=p_expdt)
        p1.save()
        return HttpResponse("product inserted sucessfully")

