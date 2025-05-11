import requests

# Test script to verify the reminders API endpoint
url = "http://127.0.0.1:8000/api/reminders/"
data = {
    "date": "2025-05-12",
    "time": "14:00:00",
    "message": "Meeting reminder",
    "reminder_type": "Email"
}

# Send a POST request to the API endpoint
response = requests.post(url, json=data)

# Print the response status code and JSON data
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
