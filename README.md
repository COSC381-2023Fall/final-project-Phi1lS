Phill Solis
Jacob Yankee
Jiang COSC 381
12.13.2023

# final-project-Phi1lS

## Description
This project consists of a FastAPI app that finds movie review videos. In total, the 
app has four API methods.

## Features
HelloWorld API method that displays the message "Hello World".
API method that finds movie reviews/commentary through YouTube Data API.
API method that gets a full description of a movie review.
API method that gets reviews in a different language.

Test methods use mocker to avoid making actual API calls.

## Usage
Install FastAPI and Uvicorn. The command using pip is the following:
pip install fastapi uvicorn

If you would like to test this applicaton, you can also install pytest and pytest-mock using the following command:
pip install pytest pytest-mock

To test the YouTube API methods, you need the Google API. To install it, you can run this command:
pip install --upgrade google-api-python-client

then run the FastAPI application using uvicorn using the follow command:
uvicorn main:app --reload

This will serve your API on http://127.0.0.1:8000
to go to SwaggerUI, go to http://127.0.0.1:8000/docs

To test the application using pytest, use the following command:
pytest

PLEASE NOTE: For now, I am keeping my YouTube API Key in a .env file locally on my PC as to avoid any potential security issues. I have emailed the professor to ask if this is okay to do instead of putting my API key on my config.py. If it turns out that this is not allowed, this will change in future issues. For now, you need to provide your own YouTube API Key.

Here is an example .env file:
import os
from dotenv import load_dotenv
load_dotenv()  # This loads the .env file at the root of the project

YOUTUBE_API_KEY = YOUR_API_KEY_HERE

## Expected Input
HelloWorld API takes no Input

API method that finds movie reviews/commentary through YouTube Data API takes a string that represents the movie name. Example: Harry Potter

API method that gets a full description of a movie review takes a string that represents the video id. Example: U3dE0sYZqvl

API method that gets reviews in a different language takes two parameters: a string that represents the language and a string that represents the movie name.
To specify a language, use iso639-1 two letter language codes, except for zh-Hans for simplified Chinese and zh-Hant for traditional Chinese.
zh-Hant for traditional Chinese. Example: en

## Program Operation
All API methods, excluding the HelloWorld API, heavily utilize the YouTube Data API to grab video names and descriptions.

## Output Format
Each API has a different expected output.

HelloWorld API outputs "message: Hello World"

API method that finds movie reviews/commentary through YouTube Data API outputs in this format:
"id": video id
"title": title of video
"description": description of video

API method that gets a full description of a movie review outputs in this format:
"description": full description of video


API method that gets reviews in a different language outputs in this format. Note that it is the same format as the method that finds movie reviews/commentary, only in a different language:
"id": video id
"title": title of video
"description": description of video

PLEASE NOTE: Putting in just a proper noun will oftentimes give a search result in your native language due to the nature of YouTube's algorithm. For example, "harry potter" will likely just give you English search results. To fix this, try searching "harry potter review" instead. Languages that don't use the latin alphabet, such as Chinese or Russian, will not have this issue.
