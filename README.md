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

PLEASE NOTE: I am keeping my YouTube API Key in a .env file locally on my PC as to avoid any potential security issues. You need to provide your own YouTube API Key.

Here is an example .env file:
import os
from dotenv import load_dotenv
load_dotenv()  # This loads the .env file at the root of the project

YOUTUBE_API_KEY = YOUR_API_KEY_HERE

PLEASE NOTE: In the case that any aspect of the program is not working, I encourage you to install all dependencies from the requirements.txt with this pip command:
pip install -r requirements.txt 

## Expected Input
HelloWorld API takes no Input

API method that finds movie reviews/commentary through YouTube Data API takes a string that represents the movie name. Example: Harry Potter

API method that gets a full description of a movie review takes a string that represents the video id. Example: U3dE0sYZqvl

API method that gets reviews in a different language takes two parameters: a string that represents the language and a string that represents the movie name.
To specify a language, use iso639-1 two letter language codes, except for zh-Hans for simplified Chinese and zh-Hant for traditional Chinese.
zh-Hant for traditional Chinese. Example: ru

## Program Operation
All API methods, excluding the HelloWorld API, heavily utilize the YouTube Data API to grab video names and descriptions.

The API method that gets reviews in a different language also uses the Google Cloud Translation API to translate the search term.

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