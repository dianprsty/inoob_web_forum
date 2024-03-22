from django.db import connection
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .helpers import cursor_to_dict, date_to_time_ago


# Create your views here.

def get_saved(user_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT title, questions.content as q_content, questions.created_at as created_at, 
                questions.id, username, saved.user_id ,
                (SELECT coalesce(count(content),0) FROM answers WHERE questions.id = answers.question_id) +
                (SELECT coalesce(count(r.content),0) FROM replies r join answers a on a.id = r.answer_id )
                as total_answers,
                (SELECT sum(vote) FROM vote_questions vq  WHERE questions.id = vq.question_id)
                as total_votes
            FROM questions
            LEFT JOIN auth_user
            ON questions.user_id = auth_user.id
            LEFT JOIN answers
            ON questions.id = answers.question_id
            LEFT JOIN replies
            ON answers.id = replies.answer_id
            LEFT JOIN saved
            ON questions.id = saved.question_id 
            WHERE saved.user_id = %s
            GROUP BY title , q_content, questions.created_at, questions.id, username, saved.user_id ; 
                       """, [user_id])
        row = cursor_to_dict.dictfetchall(cursor)
    return row

def get_question_tags(question_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT name FROM questions
            JOIN tags ON (questions.id = tags.question_id)
            JOIN categories ON (categories.id = tags.category_id)
            WHERE questions.id = %s        
                       """, [question_id])
        row = cursor_to_dict.dictfetchall(cursor)
    return row

@login_required
def saved(request):
    questions = get_saved(request.user.id)
    for index, question in enumerate(questions):
        time_ago = date_to_time_ago.to_time_ago(question["created_at"])
        tags = get_question_tags(question["id"])
        questions[index]["time_ago"] = time_ago
        questions[index]["tags"] = tags
    return render(request, "discussion/saved.html", {"questions":questions})