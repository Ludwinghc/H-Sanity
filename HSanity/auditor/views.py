from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Auditor
from .forms import AuditorForm

# Create your views here.
def inicioAuditor(request):
    return render(request, 'general/inicio.html')

def viewAuditor(request):
    auditores = Auditor.objects.all()
    return render(request, 'auditor/view.html', {'auditor' : auditores})

def create(request):
    form_auditor = AuditorForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    #     return redirect('view')
    return render(request, 'auditor/create.html', {'form_auditor' : form_auditor})

def edit(request, id):
    auditor = Auditor.objects.get(id=id)
    form = AuditorForm(request.POST or None, request.FILES or None, instance=auditor)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('view')
    return render(request, 'auditor/create.html', {'form' : form})
    return render(request, 'auditor/edit.html')
