from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Auditor
from .forms import AuditorForm

# Create your views here.
def inicioAuditor(request):
    return render(request, 'general/auditorHome.html')

def viewAuditor(request):
    auditores = Auditor.objects.get(id = 1)
    print (auditores)
    return render(request, 'auditor/viewAuditor.html', {'auditor' : auditores})

def createAuditor(request):
    form_auditor = AuditorForm(request.POST or None)
    if form_auditor.is_valid():
      form_auditor.save()
      return redirect('inicioAuditor')
    return render(request, 'auditor/createAuditor.html', {'form_auditor' : form_auditor})

def edit(request, id):
    auditor = Auditor.objects.get(id=id)
    form = AuditorForm(request.POST or None, request.FILES or None, instance=auditor)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('view')
    return render(request, 'auditor/createAuditor.html', {'form' : form})
    return render(request, 'auditor/editAuditor.html')
