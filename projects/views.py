from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from utils.DatabaseOps import sql_query


# Create your views here.

class ProjectsViewSet(viewsets.ViewSet):
    def get_projects(self, request):
        query = """
                SELECT *
                FROM projects_project
                WHERE is_active = 1;
        """
        results = sql_query(query)
        return Response(results)
