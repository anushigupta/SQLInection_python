from django.db import connection

def get_user(username):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE username = '%s'" % username)
        row = cursor.fetchone()
    return row
