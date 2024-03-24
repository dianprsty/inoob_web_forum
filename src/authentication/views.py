from django.db import connection
from django.shortcuts import render, redirect
from .forms import RegisterForm

def create_profile(user_id):
     with connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO profiles
            (user_id) VALUES (%s)
                       """, [user_id])
# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            user_id =   user.id
            create_profile(user_id)

        return redirect("login")
    else:
	    form = RegisterForm()
    return render(response, "registration/register.html", {"form": form })
