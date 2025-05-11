from rest_framework import serializers
from .models import Reminder

class ReminderSerializer(serializers.ModelSerializer):
    """
    Serializer for the Reminder model.
    Converts Reminder instances to JSON and validates input data.
    """
    class Meta:
        model = Reminder
        fields = ['id', 'date', 'time', 'message', 'reminder_type']
