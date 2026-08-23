import json
import requests

# Define a function named emotion_detector that takes a string input (text_to_analyze)
def emotion_detector(text_to_analyze):
    # Error response dictionary with all values as None
    error_response = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }

    # Handle blank entries - no input from user
    if not text_to_analyze or not text_to_analyze.strip():
        return error_response

    # URL of the emotion analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Create a dictionary with the text to be analyzed
    myobj = {"raw_document": {"text": text_to_analyze}}
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json=myobj, headers=header)

    # For status_code 400, return the same dictionary with all values as None
    if response.status_code == 400:
        return error_response

    # 304: server response for blank/invalid text — same display as blank entries (all None)
    if response.status_code == 304:
        return error_response

    if response.status_code != 200:
        return error_response

    # Parse the JSON response
    parsed = response.json()

    emotions = parsed.get("emotionPredictions", [{}])[0].get("emotion", {})
    anger_score = emotions.get("anger", 0)
    disgust_score = emotions.get("disgust", 0)
    fear_score = emotions.get("fear", 0)
    joy_score = emotions.get("joy", 0)
    sadness_score = emotions.get("sadness", 0)

    # Find dominant emotion
    emotion_scores = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion
    }
