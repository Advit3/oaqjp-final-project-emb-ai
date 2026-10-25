# Watson NLP Emotion Detector

A compact Flask application for the IBM/Coursera emotion detection final project. It calls the Watson NLP EmotionPredict service and returns anger, disgust, fear, joy, sadness, and the dominant emotion.

## Run

Install dependencies with `python -m pip install -r requirements.txt`, then launch `python server.py` and open `http://127.0.0.1:5000`.

## Test

Run `python -m unittest -v` from this folder. Watson requests are mocked in unit tests so the tests do not depend on network availability.

## API

`GET /emotionDetector?textToAnalyze=I%20am%20happy` returns JSON. Empty input returns HTTP 400 with a helpful error message.
