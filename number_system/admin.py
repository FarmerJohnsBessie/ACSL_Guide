from django.contrib import admin
from .models import Profile, SolverProfile, DailyAPICallCount
# Register your models here.
admin.site.register(Profile)
admin.site.register(SolverProfile)
admin.site.register(DailyAPICallCount)
