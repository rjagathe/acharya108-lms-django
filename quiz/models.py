from django.db import models

class Quiz(models.Model):
    lesson = models.ForeignKey('lessons.Lesson', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=200)

    def __str__(self):
        return f'Quiz for {self.lesson.title}'
