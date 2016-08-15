from builtins import list
from django.http import HttpResponse
from django.shortcuts import render
from .models import Jumachine
# from .models import Info
def adminform(request):
    return render(request,'ojlist.html')
def state(request):
    res = list(Jumachine.objects.filter())
    return render(request, 'ojlist.html',{
       'mlist': res
    })
def info(request, jid):
    machine = Jumachine.objects.filter(jid=jid).first()
    if machine == None:
        machine = []
    else:
        inf = list(machine.process.all())
        print(inf[0].ptype)
    return render(request,'info.html',{
        'info':inf
    })
