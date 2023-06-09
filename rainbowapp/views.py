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
class RainbowDispaly(View):
    def get(self,request):
        recs=Rainbow.objects.all()
        mydict={"records":recs}
        return render(request,'display.html',context=mydict)
class RainbowDeleteInput(View):
    def get(self,request):
        return render(request,'deleteinput.html')
class RainbowDelete(View):
    def get(self, request):
        p_id = int(request.GET["t1"])
        p1 = Rainbow.objects.filter(pid=p_id)
        if p1:
            p1.delete()
            return HttpResponse("product deleted successfully")
        else:
            return HttpResponse("product dosenot exists")
class RainbowUpdateInput(View):
    def get(self,request):
        return render(request,'updateinput.html')
class RainbowUpdate(View):
    def get(self,request):
        p_id = int(request.GET["t1"])
        p_name = request.GET["t2"]
        p_cost = float(request.GET["t3"])
        p_mfdt = request.GET["t4"]
        p_expdt = request.GET["t5"]
        p=Rainbow.objects.get(pid=p_id)
        p.pname=p_name
        p.pcost=p_cost
        p.pmfdt=p_mfdt
        p.pexpdt=p_expdt
        p.save()
        return HttpResponse("product update succussfully")

