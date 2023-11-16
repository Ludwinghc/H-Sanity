from django.shortcuts import render, redirect, get_object_or_404
from .models import Audit, Section, Question, Establishment, Answer, AuditFile
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from account.decorators import unauthenticatedUser, allowedUsers

import os

@login_required(login_url="login")
@allowedUsers(allowedRoles='auditor')
def audits(request, id):
    establishment = get_object_or_404(Establishment, id=id)
    audits = Audit.objects.filter(establishment=establishment)

    context = {
        "establishment": establishment,
        "audits": audits,
    }

    return render(request, "audits/audits.html", context)


def calculateSectionScore(section, answers):
    sectionScore = 0
    maxSectionScore = 0

    for question in Question.objects.filter(section=section):
        maxSectionScore += 1
        answerId = answers.get(f"question_{question.id}", None)

        if answerId:
            answer = Answer.objects.get(pk=answerId)
            if answer.correct:
                sectionScore += 1

    if maxSectionScore == 0:
        return 0
    return (sectionScore / maxSectionScore) * 100


def calculateAuditScore(answers):
    totalScore = 0
    numSections = 0

    for section in Section.objects.all():
        sectionScore = calculateSectionScore(section, answers)
        totalScore += sectionScore
        numSections += 1

    if numSections == 0:
        return 0

    return totalScore / (numSections - 1)


@login_required(login_url="login")
@allowedUsers(allowedRoles='auditor')
def createAudit(request, id):
    establishment = get_object_or_404(Establishment, id=id)
    sections = Section.objects.all()
    questions = Question.objects.all()

    if request.method == "POST":
        answers = request.POST
        audit = createNewAudit(establishment, answers)
        uploaded_files = request.FILES
        uploadFiles(uploaded_files, audit)

        return redirect("auditView", id=establishment.id)

    context = {
        "establishment": establishment,
        "sections": sections,
        "questions": questions,
    }

    return render(request, "audits/createAudit.html", context)


def createNewAudit(establishment, answers):
    auditScore = calculateAuditScore(answers)
    audit = Audit.objects.create(scoreToPass=80)
    audit.establishment.add(establishment)
    audit.score = auditScore
    audit.save()
    return audit


def uploadFiles(audit):
    
    AUDIT_FILES = [
        "RNT",
        "RUT",
        "Registro Mercantil",
        "Matricula Mercantil",
        "Comunicación Policia Nacional",
        "Uso de Suelos",
        "Targeta Registro Alojamiento",
        "Contrato Hospedaje",
        "Concepto Tecnico Bomberos",
        "Concepto Sanitario",
        "Permiso Publicidad",
        "Sayco y Acinpro",
    ]

    auditDirectory = f"media/files/audits/{audit.id}"
    os.makedirs(auditDirectory, exist_ok=True)
