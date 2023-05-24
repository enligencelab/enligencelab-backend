from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from utils.DatabaseOps import sql_query


# Create your views here.
class AchievementsViewSet(viewsets.ViewSet):
    def get_achievements(self, request):
        query = """
                SELECT achievement_name, date
                FROM achievements_achievement
                WHERE is_active = 1;
        """
        results = sql_query(query)
        return Response(results)
