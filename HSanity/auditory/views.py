from django.shortcuts import render

# Create your views here.

def audits(request):
    return render(request, "audits/audits.html")

def createAudit(request):
    return render(request, "audits/createAudit.html")
