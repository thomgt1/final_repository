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
        requests.exceptions.RequestException: If the HTTP request fails.
    """

    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    payload = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(url, json=payload, headers=headers, timeout=10)

    # Initialize dictionary so it always exists
    emotion_data = {}

    if response.status_code == 200:
        formatted_response = json.loads(response.text)

        emotion_data = formatted_response[
            "emotionPredictions"
        ][0]["emotionMentions"][0]["emotion"]

        dominant_emotion = max(emotion_data, key=emotion_data.get)
        emotion_data["dominant_emotion"] = dominant_emotion

    elif response.status_code == 400:
        # Set all expected keys to None
        for key in ("anger", "disgust", "fear", "joy", "sadness"):
            emotion_data[key] = None

        emotion_data["dominant_emotion"] = None

    elif response.status_code == 500:
        emotion_data = None

    else:
        emotion_data = None

    return emotion_data