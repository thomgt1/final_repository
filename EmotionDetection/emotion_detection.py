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
        dict: A dictionary containing emotion scores and the dominant emotion.

    Raises:
        KeyError: If the expected keys are missing in the API response.
        requests.exceptions.RequestException: If the HTTP request fails.
    """

    # Endpoint for Watson NLP EmotionPredict service
    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    # Required header specifying the Watson emotion model
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Payload containing the raw text document
    payload = {"raw_document": {"text": text_to_analyse}}

    # Send POST request to the Watson API
    response = requests.post(url, json=payload, headers=headers, timeout=10)

    emotion_date = {}
    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        # Parse JSON response
        formatted_response = json.loads(response.text)

        # Extract emotion dictionary from the first prediction
        emotion_data = formatted_response[
            "emotionPredictions"
        ][0]["emotionMentions"][0]["emotion"]

        # Determine the emotion with the highest score
        dominant_emotion = max(emotion_data, key=emotion_data.get)

        # Add dominant emotion to the dictionary
        emotion_data["dominant_emotion"] = dominant_emotion


    elif response.status_code == 400:
        for key in ('anger', 'disgust', 'fear', 'joy', 'sadness'):
            emotion_data[key] = None
        emotion_data["dominant_emotion"] = None

    elif response.status_code == 500:
        emotion_data = None
        

    else:
        emotion_data =  None

    return emotion_data