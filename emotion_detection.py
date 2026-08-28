"""Provides emotion detection functionality for customer feedback.

This module uses an AI-based emotion detection service to analyze
customer feedback and identify the emotion expressed in the text.
"""

import json
import requests

def emotion_detector(text_to_analyze):
    """Detects the emotion expressed in the given text.
    """

    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1'
        '/NlpService/EmotionPredict'
    )
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers = headers, timeout = 5)
    json_response = json.loads(response.text)

    formatted_response = {
        "anger": json_response["emotionPredictions"][0]["emotion"]["anger"],
        "disgust": json_response["emotionPredictions"][0]["emotion"]["disgust"],
        "fear": json_response["emotionPredictions"][0]["emotion"]["fear"],
        "joy": json_response["emotionPredictions"][0]["emotion"]["joy"],
        "sadness": json_response["emotionPredictions"][0]["emotion"]["sadness"]
    }

    dominant_emotion = None
    for emotion, score in formatted_response.items():
        if (
            dominant_emotion is None
            or score > formatted_response[dominant_emotion]
        ):
            dominant_emotion = emotion

    formatted_response["dominant_emotion"] = dominant_emotion

    return formatted_response
