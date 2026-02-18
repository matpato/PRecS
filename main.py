import pandas as pd
import numpy as np
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timedelta
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if os.path.exists("webpage"):
    app.mount("/webpage", StaticFiles(directory="webpage"), name="webpage")

DATASET_FILENAME = "df_recovered_with_cleaned_names.csv"
df_clean = pd.DataFrame()

CONDITION_SYNONYMS = {
    'Depression': ['sad', 'sadness', 'hopeless', 'depressed', 'crying', 'suicide'],
    'Anxiety': ['anxious', 'worry', 'panic', 'fear', 'stress', 'nervous'],
    'Pain': ['pain', 'ache', 'hurts', 'migraine', 'back', 'headache'],
    'Acne': ['pimple', 'skin', 'acne', 'breakout', 'spots'],
    'High Blood Pressure': ['pressure', 'hypertension', 'heart'],
    'Insomnia': ['sleep', 'awake', 'tired', 'insomnia', 'waking']
}

@app.on_event("startup")
def load_data():
    global df_clean
    if os.path.exists(DATASET_FILENAME):
        try:
            df = pd.read_csv(DATASET_FILENAME)
            if 'date' in df.columns:
                df['date'] = pd.to_datetime(df['date'], errors='coerce')
            df_clean = df
            print(f"✅ Dataset loaded: {len(df)} rows.")
        except Exception as e:
            print(f"❌ Dataset error: {e}")

class SymptomRequest(BaseModel):
    text: str

@app.post("/api/predict_condition")
def predict_condition(req: SymptomRequest):
    text = req.text.lower()
    found_conditions = set()
    for cond, keywords in CONDITION_SYNONYMS.items():
        for word in keywords:
            if word in text:
                found_conditions.add(cond)
    
    if not found_conditions and len(text) > 3:
        matches = df_clean[df_clean['condition'].str.lower().str.contains(text, na=False)]['condition'].unique()
        for m in matches[:5]:
            found_conditions.add(m)
    return {"conditions": list(found_conditions)}

# --- NEW ENDPOINT FOR SLIDER UPDATES ---
class ConditionStatsRequest(BaseModel):
    condition: str

@app.post("/api/condition_stats")
def get_condition_stats(req: ConditionStatsRequest):
    if df_clean.empty:
        return {"max_reviews": 0}

    mask = df_clean['condition'].str.contains(req.condition, case=False, na=False, regex=False)
    target_df = df_clean[mask]
    
    if target_df.empty:
        return {"max_reviews": 0}
        
    # Find the drug with the maximum number of reviews for this condition
    counts = target_df.groupby('drugName')['rating'].count()
    if counts.empty:
         return {"max_reviews": 0}
         
    max_v = int(counts.max())
    return {"max_reviews": max_v}

class RecommendRequest(BaseModel):
    condition: str
    limit: int = 5
    model: Optional[str] = None
    min_reviews: Optional[int] = 0
    time_filter: Optional[str] = "all"

@app.post("/api/recommend")
def get_recommendations(req: RecommendRequest):
    if df_clean.empty:
        raise HTTPException(status_code=503, detail="Dataset not loaded")

    mask = df_clean['condition'].str.contains(req.condition, case=False, na=False, regex=False)
    target_df = df_clean[mask].copy()

    if target_df.empty:
        return {"results": [], "metadata": {"max_reviews": 0}}

    if req.time_filter and req.time_filter != "all":
        cutoff_date = None
        now = datetime.now()
        
        if req.time_filter == "1-month":
            cutoff_date = now - timedelta(days=30)
        elif req.time_filter == "6-months":
            cutoff_date = now - timedelta(days=180)
        elif req.time_filter == "12-months":
            cutoff_date = now - timedelta(days=365)
        elif req.time_filter == "2-years":
            cutoff_date = now - timedelta(days=730)
        elif req.time_filter == "5-years":
            cutoff_date = now - timedelta(days=1825)
        elif req.time_filter == "10-years":
            cutoff_date = now - timedelta(days=3650)
            
        if cutoff_date:
            target_df = target_df[target_df['date'] >= cutoff_date]

    if target_df.empty:
        return {"results": [], "metadata": {"max_reviews": 0}}

    stats = target_df.groupby('drugName').agg(
        R=('rating', 'mean'),
        v=('rating', 'count')
    ).reset_index()

    if req.min_reviews and req.min_reviews > 0:
        stats = stats[stats['v'] >= req.min_reviews]

    if stats.empty:
        return {"results": [], "metadata": {"max_reviews": 0}}

    max_v = float(stats['v'].max())
    if max_v == 0: max_v = 1.0

    C = target_df['rating'].mean()
    m = 5 
    stats['bayesian'] = (stats['v'] * stats['R'] + m * C) / (stats['v'] + m)
    
    stats['confidence'] = stats['v'] / max_v

    top_drugs = stats.sort_values(by='bayesian', ascending=False).head(req.limit)

    results = []
    rank = 1
    for _, row in top_drugs.iterrows():
        results.append({
            "rank": rank,
            "drug": row['drugName'],
            "condition": req.condition,
            "score": round(row['R'], 2),
            "weighted_rating": round(row['bayesian'], 2),
            "confidence": round(row['confidence'] * 100, 1),
            "sample_size": int(row['v'])
        })
        rank += 1

    return {
        "results": results,
        "metadata": {
            "max_reviews": int(max_v)
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)