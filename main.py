from fastapi import FastAPI, HTTPException
from typing import List
from youtube import search_movie_reviews

app = FastAPI()

# Hello World API method
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/moviereviews/{movie_name}", response_model=List[dict])
async def get_movie_reviews(movie_name: str):
    try:
        reviews = search_movie_reviews(movie_name)
        return reviews
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))