from fastapi.testclient import TestClient
from main import app
from youtube import search_movie_reviews
import pytest
from unittest.mock import patch

client = TestClient(app)

def test_read_main():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello World'}

@pytest.fixture
def mock_search_movie_reviews(mocker):
    mock = mocker.patch('main.search_movie_reviews', autospec=True)
    mock.return_value = [
        {
            'id': 'video_id_1',
            'title': 'Review 1',
            'description': 'Description of review 1'
        }
    ]
    return mock

def test_get_movie_reviews(mock_search_movie_reviews):
    movie_name = 'test_movie'
    response = client.get(f'/moviereviews/{movie_name}')
    assert response.status_code == 200
    assert response.json() == mock_search_movie_reviews.return_value
    mock_search_movie_reviews.assert_called_once_with(movie_name)

def test_video_description():
    # Get response from valid video id
    response = client.get('/descriptions/U3dE0sYZqvI')

    # Assert the response status code and content
    assert response.status_code == 200
    assert response.json() != {'description': 'Description not found.'}

def test_video_description_no_description():
    # Get response from valid video id
    response = client.get('/descriptions/wow')

    # Assert the response status code and content
    assert response.status_code == 200
    assert response.json() == {'description': 'Description not found.'}
