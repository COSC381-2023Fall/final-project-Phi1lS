from googleapiclient.discovery import build
from config import YOUTUBE_API_KEY

# Method that returns id, title, and description from name
def search_movie_reviews(movie_name):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    
    request = youtube.search().list(
        part='snippet',
        q=f'{movie_name} review',
        type='video',
        maxResults=10,
        order='relevance',
        safeSearch='moderate'
    )
    
    response = request.execute()

    videos = []
    for item in response.get('items', []):
        video_id = item['id']['videoId']
        video_title = item['snippet']['title']
        video_description = item['snippet']['description']
        
        videos.append({
            'id': video_id,
            'title': video_title,
            'description': video_description
        })
    
    return videos

# Method that returns video description from video id
def get_video_description(video_id):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

    request = youtube.videos().list(
        part='snippet',
        id=video_id
    )

    response = request.execute()

    if response.get('items'):
        description = response['items'][0]['snippet']['description']
    else:
        description = 'Description not found.'

    return description
