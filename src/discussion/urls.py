from django.urls import path
from .views import dashboard_views

urlpatterns = [
    path("dashboard/", dashboard_views.dashboard, name="dashboard"),
    # view discussion bisa diubah ke custom view mas satya
    path('discussion/detail/<int:id>', dashboard_views.dashboard, name='detail'),

]
