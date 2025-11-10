from fastapi import FastAPI

app = FastAPI(
    title="UZ-RealTime API",
    description="Real-time object detection platform",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "UZ-RealTime ishlayapti!",
        "status": "active",
        "time": "2025-11-10 13:36"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
