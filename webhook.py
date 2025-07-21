from fastapi import FastAPI, Request, Header, HTTPException
from dotenv import load_dotenv
import os, requests

load_dotenv()
SECRET = os.getenv("WEBHOOK_SECRET")

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request, authorization: str = Header(None)):
    if authorization != f"Bearer {SECRET}":
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    payload = await request.json()
    print("✅ Webhook received:", payload)

    if payload.get("event_type") == "meeting.transcript":
        transcript_url = payload["data"]["transcript_url"]
        text = requests.get(transcript_url).text
        print("📝 Transcript:\n", text[:500])
    
    return {"status": "received"}
