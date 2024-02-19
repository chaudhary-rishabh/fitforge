# admin.py

from django.contrib import admin
from .models import GoalPlan, DietPlan

admin.site.register(GoalPlan)
admin.site.register(DietPlan)
