from django.urls import path
from .views import PeopleViewSet

urlpatterns = [
    path('teachers', PeopleViewSet.as_view({'get': 'get_teachers'})),
    path('graduates', PeopleViewSet.as_view({'get': 'get_graduates'})),
    path('undergraduates', PeopleViewSet.as_view({'get': 'get_undergraduates'})),
]
