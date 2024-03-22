from django.urls import path
from .views import dashboard_views, my_qna_view, saved_view

urlpatterns = [
    path("dashboard/", dashboard_views.dashboard, name="dashboard"),
    path("myqna/", my_qna_view.my_qna, name="myqna"),
    path("saved/", saved_view.saved, name="saved"),
    # view discussion bisa diubah ke custom view mas satya
    path('discussion/detail/<int:id>', dashboard_views.dashboard, name='detail'),

]
