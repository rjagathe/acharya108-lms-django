from django.shortcuts import render
from .models import Quiz

def quiz_view(request):
    quizzes = Quiz.objects.select_related('lesson').all()
    return render(request, 'quiz/quiz.html', {'quizzes': quizzes})
