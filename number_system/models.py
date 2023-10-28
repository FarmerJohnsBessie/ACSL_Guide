from django.db import models

# Create your models here.
class Question(models.Model):
    TYPE_CHOICES = (
        ("Computer Number Systems", "Computer Number Systems"),
        ("Recursive Functions", "Recursive Functions"),
        ("What Does This Program Do?", "What Does This Program Do?"),
        ("Prefix/Infix/Postfix Notation", "Prefix/Infix/Postfix Notation"),
        ("Bit-String Flicking", "Bit-String Flicking"),
        ("LISP", "LISP"),
        ("Boolean Algebra", "Boolean Algebra"),
        ("Data Structures", "Data Structures"),
        ("Regular Expressions", "Regular Expressions"),
        ("Graph Theory", "Graph Theory"),
        ("Digital Electronics", "Digital Electronics"),
        ("Assembly Language", "Assembly Language"),
    )
    question_statement = models.TextField(max_length=255)
    type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    is_multiple_choice = models.BooleanField(default=False)
    correct_answer = models.CharField(max_length=255)
    num_choices = models.PositiveIntegerField(null=True, blank=True)
    choices = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.question_statement
