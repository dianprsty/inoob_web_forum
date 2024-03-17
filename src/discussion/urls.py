from django.urls import path
from .views import dashboard_views

urlpatterns = [
    path("dashboard/", dashboard_views.dashboard, name="dashboard"),
]
