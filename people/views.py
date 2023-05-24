from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from utils.DatabaseOps import sql_query


# Create your views here.
class PeopleViewSet(viewsets.ViewSet):
    def get_teachers(self, request):
        query = """
                SELECT
                    user.id, 
                    user.username,
                    user.date_joined,
                    user.is_teacher,
                    user.github_account,
                    user.department,
                    user.school,
                    user.title,
                    user.avatar
                FROM (auth_user au inner join people_userprofile pu on au.id = pu.user_id) user
                WHERE user.is_active = 1 and user.is_teacher = 1;
        """
        results = sql_query(query)
        return Response(results)

    def get_graduates(self, request):
        query = """
                SELECT
                    user.id, 
                    user.username,
                    user.date_joined,
                    user.graduated_date,
                    user.is_graduated,
                    user.github_account,
                    user.department,
                    user.school,
                    user.avatar
                FROM (auth_user au inner join people_userprofile pu on au.id = pu.user_id) user
                WHERE user.is_active = 1 and user.is_graduated = 1;
        """
        results = sql_query(query)
        return Response(results)

    def get_undergraduates(self, request):
        query = """
                SELECT 
                    user.id,
                    user.username,
                    user.date_joined,
                    user.is_undergraduate,
                    user.github_account,
                    user.department,
                    user.school,
                    user.avatar
                FROM (auth_user au inner join people_userprofile pu on au.id = pu.user_id) user
                WHERE user.is_active = 1 and user.is_undergraduate = 1;
        """
        results = sql_query(query)
        return Response(results)
