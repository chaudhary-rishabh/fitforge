# models.py

from django.db import models

class GoalPlan(models.Model):
    goal = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    complete = models.BooleanField(default=False)

class DietPlan(models.Model):
    sr_no = models.IntegerField()
    time = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    big_message = models.TextField()
    complete = models.BooleanField(default=False)
