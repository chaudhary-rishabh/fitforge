# views.py

from rest_framework import generics
from .models import GoalPlan, DietPlan
from .serializers import GoalPlanSerializer, DietPlanSerializer

class GoalPlanListCreateView(generics.ListCreateAPIView):
    queryset = GoalPlan.objects.all()
    serializer_class = GoalPlanSerializer

class GoalPlanRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GoalPlan.objects.all()
    serializer_class = GoalPlanSerializer

class DietPlanListCreateView(generics.ListCreateAPIView):
    queryset = DietPlan.objects.all()
    serializer_class = DietPlanSerializer

class DietPlanRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DietPlan.objects.all()
    serializer_class = DietPlanSerializer
