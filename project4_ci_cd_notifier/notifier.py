import requests

WEBHOOK_URL = "https://hooks.slack.com/services/your/webhook/url"

message = {
    "text": "CI/CD Pipeline Status: SUCCESS ✅"
}

response = requests.post(WEBHOOK_URL, json=message)

print(response.status_code)