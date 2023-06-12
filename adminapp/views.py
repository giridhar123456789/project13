from django.shortcuts import render
from django.views import View
from .models import Jobs
# Create your views here.
class Home(View):
    def get(self,request):
        qs=Jobs.objects.all()
        con_dic={'records':qs}
        return render(request,'display.html',context=con_dic)