# Remind-me-later

## Project Overview
The "Remind-me-later" project is a simple web application that allows users to set up reminders with a message. Users can specify the date, time, and message content, as well as the method of notification (currently supporting SMS and Email). This project provides an API endpoint to save reminders to the database.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/ankur4290/Remind_ME_Later.git
   cd Remind_ME_Later
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000/`.

## API Endpoint Details

### Create Reminder
- **URL**: `/api/reminders/`
- **Method**: `POST`
- **Request Body** (JSON):
  ```json
  {
      "date": "YYYY-MM-DD",
      "time": "HH:MM:SS",
      "message": "Your reminder message",
      "reminder_type": "SMS or Email"
  }
  ```
- **Response** (JSON):
  ```json
  {
      "id": 1,
      "date": "YYYY-MM-DD",
      "time": "HH:MM:SS",
      "message": "Your reminder message",
      "reminder_type": "SMS or Email"
  }
  ```

## Sample Request and Response

### Request
```bash
curl -X POST http://127.0.0.1:8000/api/reminders/ \
-H "Content-Type: application/json" \
-d '{"date": "2025-05-12", "time": "14:00:00", "message": "Meeting reminder", "reminder_type": "Email"}'
```

### Response
```json
{
    "id": 1,
    "date": "2025-05-12",
    "time": "14:00:00",
    "message": "Meeting reminder",
    "reminder_type": "Email"
}
```

## Database Schema
The `Reminder` model has the following fields:
- `date` (DateField): The date of the reminder.
- `time` (TimeField): The time of the reminder.
- `message` (TextField): The message content of the reminder.
- `reminder_type` (CharField): The type of reminder (e.g., SMS, Email).

## Dependencies
All dependencies are listed in the `requirements.txt` file. Install them using:
```bash
pip install -r requirements.txt
```
