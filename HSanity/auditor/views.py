from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Auditor
from .forms import AuditorForm

# Create your views here.
# Vista para la pagina main del auditor
def inicioAuditor(request):
    return render(request, 'general/auditorHome.html')

# Vista la cual apunta a la pagina de creacion de perfil del auditor
def createAuditor(request):
    form_auditor = AuditorForm(request.POST or None)
    if form_auditor.is_valid():
        form_auditor.save()
        return redirect('inicioAuditor')
    return render(request, 'auditor/createAuditor.html', {'form_auditor' : form_auditor})


def viewAuditor(request, id=1):
    auditores = Auditor.objects.get(id = id)
    form_auditor = AuditorForm(request.POST or None, instance = auditores)
    if  request.POST:
        form_auditor.save()
        return redirect('inicioAuditor')
    return render(request, 'auditor/viewAuditor.html', {'auditor' : auditores, 'form_auditor' : form_auditor})
