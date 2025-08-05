from fastapi import APIRouter, Query
from app.services.sentiment_analyzer import analyze_sentiment

router = APIRouter()

@router.get("/analyze/")
def analyze(text: str = Query(..., description="Comment to analyze")):
    sentiment = analyze_sentiment(text)
    return {"text": text, "sentiment": sentiment}