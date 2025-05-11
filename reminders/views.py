from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Reminder
from .serializers import ReminderSerializer

# Create your views here.

class ReminderCreateView(APIView):
    """
    API view to handle the creation of reminders.

    Methods:
        post: Handles POST requests to create a new reminder.
    """
    def post(self, request):
        # Deserialize and validate the incoming data
        serializer = ReminderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the valid data to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
