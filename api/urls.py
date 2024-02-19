# urls.py

from django.urls import path
from .views import GoalPlanListCreateView, GoalPlanRetrieveUpdateDestroyView, DietPlanListCreateView, DietPlanRetrieveUpdateDestroyView

urlpatterns = [
    path('goal-plans/', GoalPlanListCreateView.as_view(), name='goalplan-list-create'),
    path('goal-plans/<int:pk>/', GoalPlanRetrieveUpdateDestroyView.as_view(), name='goalplan-detail'),
    path('diet-plans/', DietPlanListCreateView.as_view(), name='dietplan-list-create'),
    path('diet-plans/<int:pk>/', DietPlanRetrieveUpdateDestroyView.as_view(), name='dietplan-detail'),
]
