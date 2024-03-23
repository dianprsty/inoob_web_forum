from django.urls import path
from .views import dashboard_views, my_qna_view, post_question_view, saved_view, profile_view

urlpatterns = [
    path("dashboard/", dashboard_views.dashboard, name="dashboard"),
    path("postquestion/", post_question_view.post_question, name="post_question"),
    path("myqna/", my_qna_view.my_qna, name="myqna"),
    path("saved/", saved_view.saved, name="saved"),
    path("profile/", profile_view.profile, name="profile"),
    # view discussion bisa diubah ke custom view mas satya
    path('discussion/detail/<int:id>', dashboard_views.dashboard, name='detail'),

]
