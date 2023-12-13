import pytest
from unittest.mock import Mock
from googleapiclient.discovery import build
from youtube import search_movie_reviews

def test_search_movie_reviews(mocker):
    # Mock the build function to return a mock object
    mock_build = mocker.patch('googleapiclient.discovery.build')

    # Mock for the YouTube API response with 10 items
    youtube_response = {
        "items": [
            {
                "id": {"videoId": f"video{i}"},
                "snippet": {
                    "title": f"Review {i}",
                    "description": f"Description of review {i}"
                }
            } for i in range(10)  # Generating 10 items for the mock response
        ]
    }

    # Mock the execute method to return the youtube_response
    mock_build().search().list().execute.return_value = youtube_response

    # Call search_movie_reviews function with a test query
    results = search_movie_reviews("Harry Potter")

    # Assert the expected outcomes from the function
    assert len(results) == 10  # Now it checks if ten results are returned