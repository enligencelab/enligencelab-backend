from django.urls import path
from .views import PatentsViewSet

urlpatterns = [
    path('', PatentsViewSet.as_view({'get': 'get_patents'})),
]