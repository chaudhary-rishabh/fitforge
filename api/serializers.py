# serializers.py

from rest_framework import serializers
from .models import GoalPlan, DietPlan

class GoalPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalPlan
        fields = '__all__'

class DietPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietPlan
        fields = '__all__'
