from fastapi import FastAPI, HTTPException
from typing import List, Dict
from youtube import search_movie_reviews, get_video_description, search_movie_reviews_in_language

app = FastAPI()

# Hello World API method
@app.get('/')
async def root():
    return {'message': 'Hello World'}

# Find commentary/reviews from name method
@app.get('/moviereviews/{movie_name}', response_model=List[dict])
async def get_movie_reviews(movie_name: str):
    try:
        reviews = search_movie_reviews(movie_name)
        return reviews
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Find description from video id method
@app.get('/descriptions/{video_id}', response_model=Dict[str, str])
async def video_description(video_id: str):
    try:
        description = get_video_description(video_id)
        if description:
            return {'description': description}
        else:
            raise HTTPException(status_code=404, detail='Description not found')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get reviews in a different language method
@app.get('/moviereviews/{language}/{movie_name}', response_model=List[dict])
async def get_movie_reviews_in_language(language: str, movie_name: str):
    try:
        translated_reviews = search_movie_reviews_in_language(language, movie_name)
        return translated_reviews
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
