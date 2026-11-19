
from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(title="grba33 Loader Server")

@app.get("/")
def home():
    return {
        "name": "grba33 Loader",
        "status": "online",
        "version": "1.0"
    }

@app.get("/health")
def health():
    return {
        "status": "ok",
        "server": "grba33",
        "time": datetime.now(timezone.utc).isoformat()
    }

@app.get("/trial/status")
def trial_status():
    return {
        "status": "test",
        "activation_required": False,
        "message": "Development server only"
    }
