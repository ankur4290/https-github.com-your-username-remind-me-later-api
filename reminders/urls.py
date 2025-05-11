from django.urls import path
from . import views

# URL configuration for the reminders app
urlpatterns = [
    path('', views.ReminderCreateView.as_view(), name='create_reminder'),  # Endpoint to create reminders
]
