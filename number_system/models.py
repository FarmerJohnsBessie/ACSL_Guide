from django.db import models

# Create your models here.
class Question(models.Model):
    question_statement = models.CharField(max_length=255)
    is_multiple_choice = models.BooleanField(default=False)
    correct_answer = models.CharField(max_length=255)
    num_choices = models.PositiveIntegerField(null=True, blank=True)
    choices = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.question_statement
