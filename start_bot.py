import requests
import os
from dotenv import load_dotenv

load_dotenv()

RECALL_API_KEY = os.getenv("RECALL_API_KEY")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

def start_meeting_bot(meeting_url, platform):
    url = "https://api.recall.ai/api/v1/meetings/start"
    headers = {
        "Authorization": f"Token {RECALL_API_KEY}",
        "Content-Type": "application/json"
    }
    body = {
        "platform": platform,
        "meeting_url": meeting_url,
        "webhook_url": WEBHOOK_URL
    }

    response = requests.post(url, json=body, headers=headers)
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.json())

# Example:
# start_meeting_bot("https://zoom.us/j/1234567890", "zoom")
