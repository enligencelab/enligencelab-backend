from django.urls import path
from .views import ProjectsViewSet

urlpatterns = [
    path('', ProjectsViewSet.as_view({'get': 'get_projects'})),
]