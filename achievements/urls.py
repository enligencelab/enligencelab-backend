from django.urls import path
from .views import AchievementsViewSet

urlpatterns = [
    path('', AchievementsViewSet.as_view({'get': 'get_achievements'})),
]