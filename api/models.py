from django.db import models

# Create your models here.
class Question(models.Model):
    TYPE_CHOICES = (
        ("Computer_Number_Systems", "Computer Number Systems"),
        ("Recursive_Functions", "Recursive Functions"),
        ("What_Does_This_Program_Do", "What Does This Program Do?"),
        ("Prefix_Infix_Postfix_Notation", "Prefix/Infix/Postfix Notation"),
        ("Bit-String_Flicking", "Bit-String Flicking"),
        ("LISP", "LISP"),
        ("Boolean_Algebra", "Boolean Algebra"),
        ("Data_Structures", "Data Structures"),
        ("Regular_Expressions", "Regular Expressions"),
        ("Graph_Theory", "Graph Theory"),
        ("Digital_Electronics", "Digital Electronics"),
        ("Assembly_Language", "Assembly Language"),
    )
    question = models.TextField(max_length=10000)
    type = models.CharField(max_length=30, choices=TYPE_CHOICES, null=False)
    is_multiple_choice = models.BooleanField(default=False)
    steps = models.TextField(max_length=10000, null=True, blank=True)
    answer = models.CharField(max_length=255)
    likes = models.IntegerField(blank=False, null=False, default=0)
    difficulty = models.IntegerField(blank=False, null=False, default=1)
    num_choices = models.PositiveIntegerField(null=True, blank=True)
    choices = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.question