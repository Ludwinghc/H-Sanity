from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import (
    Audit,
    Section,
    Question,
    Establishment,
    Answer,
    AuditResult,
    SectionResult,
)
from django.db.models import Avg


# Create your views here.


def audits(request, id):
    establishment = get_object_or_404(Establishment, id=id)
    audits = Audit.objects.filter(establishment=establishment)

    context = {
        "establishment": establishment,
        "audits": audits,
    }

    return render(request, "audits/audits.html", context)


def createAudit(request, id):

    establishment = get_object_or_404(Establishment, id=id)
    sections = Section.objects.all()
    questions = Question.objects.all()

    if request.method == 'POST':
        # Crear una nueva auditoría
        audit = Audit.objects.create(scoreToPass=80)  # Create the Audit instance without the establishment
        audit.establishment.add(establishment) # Add the establishment relationship separately
        # Recopila los datos del formulario y calcula el puntaje    
        total_score = 0
        for section in Section.objects.all():
            section_score = 0
            for question in Question.objects.filter(section=section):
                answer_id = request.POST.get(f'question_{question.id}', None)
                if answer_id:
                    answer = Answer.objects.get(pk=answer_id)
                    if answer.correct:
                        section_score += 1  # Incrementa el puntaje en 1 por cada respuesta correcta

            total_score += section_score

        # Calcula el puntaje promedio de la auditoría
        num_sections = Section.objects.count()
        audit_score = total_score / num_sections

        # Guarda el puntaje total en el campo score de la auditoría
        audit.score = audit_score
        audit.save()

        return redirect('auditView', id=establishment.id)

    context = {
        'establishment': establishment, 
        'sections': sections,
        'questions': questions
        }
    
    return render(request, "audits/createAudit.html", context)


# def auditDetail(request, id):
#     audit = Audit.objects.get(id=id)
#     section_results = SectionResult.objects.filter(section__audit=audit)
#     audit_result = AuditResult.objects.get(audit=audit)

#     context = {
#         "audit": audit,
#         "section_results": section_results,
#         "audit_result": audit_result,
#     }

#     return render(request, "audit_detail.html", context)
