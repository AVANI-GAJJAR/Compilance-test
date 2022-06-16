import re,ftplib
from django.shortcuts import render
from django.http import HttpResponse
from PPI.models import IngestData
#from PPI.models import ppi
# Create your views here.
def index(request):
    return render(request,'login.html')

def filetype(request):
   saved = False
   if request.method == "POST":
      #Get the posted form
      MyForm = IngestData(request.POST, request.FILES)
      
      if MyForm.is_valid():
         obj= IngestData()
         obj.fname = MyForm.cleaned_data["filename"]
         obj.save()
         saved = True
   else:
      MyForm = IngestData()
		
   return render(request, 'saved.html', locals())
def auth(request):
    if request.method== "POST":
        nm=request.POST.get('username')
        pwd=request.POST.get('password')
        if nm=="ddx1" and pwd=="Demo":
            return render(request,'ingest.html')
        
    return HttpResponse("error")

