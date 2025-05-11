from django.db import models

class Reminder(models.Model):
    """
    A model to store reminder details.

    Attributes:
        date (DateField): The date of the reminder.
        time (TimeField): The time of the reminder.
        message (TextField): The message content of the reminder.
        reminder_type (CharField): The type of reminder (e.g., SMS, Email).
    """
    REMINDER_TYPES = [
        ('SMS', 'SMS'),
        ('Email', 'Email'),
    ]

    date = models.DateField(help_text="Date of the reminder")
    time = models.TimeField(help_text="Time of the reminder")
    message = models.TextField(help_text="Message content of the reminder")
    reminder_type = models.CharField(max_length=10, choices=REMINDER_TYPES, help_text="Type of reminder (SMS or Email)")

    def __str__(self):
        return f"{self.date} {self.time} - {self.reminder_type}"
