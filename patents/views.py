from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from utils.DatabaseOps import sql_query


# Create your views here.
class PatentsViewSet(viewsets.ViewSet):
    def get_patents(self, request):
        query = """
                SELECT patent_name, date, patent_photo
                FROM patents_patent
                WHERE is_active = 1;
        """
        results = sql_query(query)
        return Response(results)
