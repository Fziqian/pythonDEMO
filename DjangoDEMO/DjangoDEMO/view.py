from django.http import HttpResponse
from django.shortcuts import render
 
def hello(request):
    context={}
    context['hello']='hello world'
    return render(request,'hello.html',context)
def ifelse(request):
    context={'flag':1==1}
    context['list']=range(5)
    return render(request,'ifelse.html',context)