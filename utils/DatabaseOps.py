from django.db import connection


def sql_query(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()

    data = []
    for row in rows:
        data.append(dict(zip(columns, row)))

    return data
