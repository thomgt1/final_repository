"""
Emotion detection module.

This module provides a wrapper around the Watson NLP EmotionPredict API.
It sends text for analysis and returns a dictionary containing emotion scores
along with the computed dominant emotion.
"""

import json
import requests


def emotion_detector(text_to_analyse: str) -> dict:
    """
    Analyze the emotional content of a given text using the Watson NLP API.

    Args:
        text_to_analyse (str): The input text to be evaluated.

    Returns:
        tuple: (emotion_data, status_code)
               emotion_data is a dictionary containing emotion scores and
               the dominant emotion, or None if the service fails.
               status_code is the HTTP status returned by the Watson API.
    """

    # Endpoint for the Watson NLP EmotionPredict service
    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    # Required header specifying the Watson emotion model
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Payload containing the raw text document to analyze
    payload = {"raw_document": {"text": text_to_analyse}}

    # Send POST request to the Watson API
    response = requests.post(url, json=payload, headers=headers, timeout=10)

    # Initialize dictionary so it always exists before branching
    emotion_data = {}

    # Successful response: extract emotion scores
    if response.status_code == 200:
        # Parse JSON response body
        formatted_response = json.loads(response.text)

        # Navigate to the emotion scores inside the response structure
        emotion_data = formatted_response[
            "emotionPredictions"
        ][0]["emotionMentions"][0]["emotion"]

        # Compute the dominant emotion by selecting the highest score
        dominant_emotion = max(emotion_data, key=emotion_data.get)

        # Add dominant emotion to the dictionary
        emotion_data["dominant_emotion"] = dominant_emotion

    # Client error: API could not process the input text
    elif response.status_code == 400:
        # Populate all expected emotion keys with None values
        for key in ("anger", "disgust", "fear", "joy", "sadness"):
            emotion_data[key] = None

        # No dominant emotion can be computed
        emotion_data["dominant_emotion"] = None

    # Server error or unexpected status codes
    else:
        # Return None to indicate failure
        emotion_data = None

    # Return both the parsed data and the API status code
    return (emotion_data, response.status_code)
