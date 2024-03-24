from django.shortcuts import render, redirect
from django.db import connection
from django.utils import timezone

def insert_question(user_id,title,content,created_at,updated_at):
    with connection.cursor() as cursor:
        cursor.execute("""
            insert into questions (user_id,title,content,created_at,updated_at) values (%s,%s,%s,%s,%s)
                       """, [user_id,title,content,created_at,updated_at])


def post_question(request):
    if request.method == 'POST':
         user_id = request.user.id
         title = request.POST['title']
         content = request.POST['content']
         print (user_id,title,content)
         insert_question (user_id,title,content,timezone.make_aware(timezone.now()),timezone.make_aware(timezone.now()))
    
        
         return redirect('dashboard')  # Redirect to success page after posting question
    
    return render(request, 'discussion/post_question.html')
