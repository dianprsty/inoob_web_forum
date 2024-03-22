from django.db import connection
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .helpers import cursor_to_dict, date_to_time_ago


# Create your views here.

def get_profile():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT name, about, username, email
            FROM profiles
            JOIN auth_user
            ON auth_user.id = profiles.user_id
                       """)
        row = cursor_to_dict.dictfetchall(cursor)
    return row



@login_required
def profile(request):
    user_profile = get_profile()[0]
    return render(request, "discussion/profile.html", {"profile": user_profile})