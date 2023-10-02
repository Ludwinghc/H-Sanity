from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Auditor
from .forms import AuditorForm

# Create your views here.

def home(request):
    return render(request, 'account/auditor/dashboard.html')

def createAuditor(request):
    form_auditor = AuditorForm(request.POST or None)
    if form_auditor.is_valid():
        form_auditor.save()
        return redirect('inicioAuditor')
    return render(request, 'account/auditor/createAuditor.html', {
        'form_auditor' : form_auditor})

def viewAuditor(request):
    auditores = Auditor.objects.get(id = 1)
    form_auditor = AuditorForm(request.POST or None, instance = auditores)
    if form_auditor.is_valid() and request.POST:
        form_auditor.save()
        return redirect('inicioAuditor')
    return render(request, 'account/auditor/viewAuditor.html', {
        'auditor' : auditores, 'form_auditor' : form_auditor})