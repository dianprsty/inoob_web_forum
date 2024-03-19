from django.db import connection
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .helpers import cursor_to_dict, date_to_time_ago


# Create your views here.

def get_question():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT title, content, questions.created_at as created_at, questions.id,
                username
            FROM questions
            JOIN auth_user
            ON questions.user_id = auth_user.id;
                       """)
        row = cursor_to_dict.dictfetchall(cursor)
    return row

@login_required
def dashboard(request, id=1):
    questions = get_question()
    time_ago = date_to_time_ago.to_time_ago(questions[0]["created_at"])
    return render(request, "discussion/dashboard.html", {"questions":questions, "time": time_ago})