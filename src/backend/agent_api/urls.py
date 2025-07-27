from django.urls import path
from . import views

urlpatterns = [
     path("", views.AgentAPIView.as_view(), name="agent-endpoint"),
]
