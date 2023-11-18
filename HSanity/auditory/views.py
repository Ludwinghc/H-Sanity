from django.shortcuts import render, redirect, get_object_or_404
from .models import Audit, Section, Question, Establishment, Answer, SectionResult
from django.core.files.storage import FileSystemStorage
from .forms import FileUploadForm
from django.contrib.auth.decorators import login_required
from account.decorators import unauthenticatedUser, allowedUsers

import os


@login_required(login_url="login")
@allowedUsers(allowedRoles="auditor")
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


def saveSectionResults(audit, answers):
    for section in Section.objects.all()[1:]:
        sectionScore = calculateSectionScore(section, answers)
        SectionResult.objects.create(audit=audit, section=section, score=sectionScore)


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
@allowedUsers(allowedRoles="auditor")
def createAudit(request, id):
    establishment = get_object_or_404(Establishment, id=id)
    sections = Section.objects.all()
    questions = Question.objects.all()
    files = FileUploadForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and files.is_valid():
        answers = request.POST
        audit = createNewAudit(establishment, answers)
        uploadFiles(request.FILES, audit)
        
        return redirect("auditView", id=establishment.id)

    context = {
        "establishment": establishment,
        "sections": sections,
        "questions": questions,
        "files": files,
    }

    return render(request, "audits/createAudit.html", context)


def createNewAudit(establishment, answers):
    auditScore = calculateAuditScore(answers)
    audit = Audit.objects.create(scoreToPass=80)
    audit.establishment.add(establishment)
    audit.score = auditScore
    audit.save()
    saveSectionResults(audit, answers)

    return audit


def uploadFiles(uploadedFiles, audit):
    auditDirectory = f"media/files/audits/{audit.id}"
    os.makedirs(auditDirectory, exist_ok=True)

    for file_field in uploadedFiles:
        file = uploadedFiles[file_field]
        file_path = os.path.join(auditDirectory, file.name)
        with open(file_path, "wb+") as destination:
            for chunk in file.chunks():
                destination.write(chunk)
