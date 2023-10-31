from django.shortcuts import render, redirect, get_object_or_404
from .models import Audit, Section, Question, Establishment, Answer, AuditFile
from django.core.files.storage import FileSystemStorage
import os


def audits(request, id):
    establishment = get_object_or_404(Establishment, id=id)
    audits = Audit.objects.filter(establishment=establishment)

    context = {
        "establishment": establishment,
        "audits": audits,
    }

    return render(request, "audits/audits.html", context)


def calculateAuditScore(answers):
    totalScore = 0

    for section in Section.objects.all():
        sectionScore = 0
        for question in Question.objects.filter(section=section):
            answerId = answers.get(f"question_{question.id}", None)
            if answerId:
                answer = Answer.objects.get(pk=answerId)
                if answer.correct:
                    sectionScore += 1

        totalScore += sectionScore

    numSections = Section.objects.count()
    auditScore = totalScore / numSections
    return auditScore


def createAudit(request, id):
    establishment = get_object_or_404(Establishment, id=id)
    sections = Section.objects.all()
    questions = Question.objects.all()

    if request.method == "POST":
        answers = request.POST  # Recopila los datos del formulario
        auditScore = calculateAuditScore(answers)

        # Crear una nueva auditoría y guardar el puntaje
        audit = Audit.objects.create(scoreToPass=80)
        audit.establishment.add(establishment)
        audit.score = auditScore
        audit.save()

        auditDirectory = f"media/audits/"
        #{audit.id}
        #os.makedirs(auditDirectory)

        AUDIT_FILES = [
            'RNT',
            'RUT',
            'Registro Mercantil',
            'Matricula Mercantil',
            'Comunicación Policia Nacional',
            'Uso de Suelos',
            'Targeta Registro Alojamiento',
            'Contrato Hospedaje',
            'Concepto Tecnico Bomberos',
            'Concepto Sanitario',
            'Permiso Publicidad',
            'Sayco y Acinpro'
        ]

        # Procesar y guardar archivos en la sección uno
        for fileField in AUDIT_FILES:
            if fileField in request.FILES:
                uploadedFile = request.FILES[fileField]
                fs = FileSystemStorage(location=auditDirectory)
                fileName = fs.save(uploadedFile.name, uploadedFile)
                
                # Crea un registro de archivo de auditoría en la base de datos
                auditFile = AuditFile(audit=audit, file=fileName)
                auditFile.save()

        return redirect("auditView", id=establishment.id)

    context = {
        "establishment": establishment,
        "sections": sections,
        "questions": questions,
    }

    return render(request, "audits/createAudit.html", context)
