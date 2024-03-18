from django.db import connection
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .helper import dictfetchall

# Create your views here.


def get_question():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM questions;
                       """)
        row = dictfetchall(cursor)
    return row

@login_required
def dashboard(request, id=1):
    questions = get_question()
    return render(request, "discussion/dashboard.html", {"questions":questions})