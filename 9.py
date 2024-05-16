from django.http import HttpResponse
from django.db import connection

def user_login(request):
    username = request.GET['username']
    password = request.GET['password']

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = '%s' AND password = '%s'" % (username, password))
    user = cursor.fetchone()

    if user:
        return HttpResponse("User logged in.")
    else:
        return HttpResponse("Invalid credentials.")
