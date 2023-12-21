from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

from api.models import Question


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    is_premium = models.BooleanField
    def __str__(self):
        return self.user.username

class Subscription(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()


class SolverProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    questions_solved = models.ManyToManyField(Question, blank=True)
    @property
    def number_of_questions_solved(self):
        return self.questions_solved.count()

    def __str__(self):
        return f'{self.user.username}\'s Solver Profile'


class DailyAPICallCount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    request_count = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if self._state.adding:
            # Delete any previous records for the same user
            DailyAPICallCount.objects.filter(user=self.user).exclude(date=timezone.now().date()).delete()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username}\'s API Call Count for {self.date}'