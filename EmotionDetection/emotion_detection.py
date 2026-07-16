import requests
import json


def emotion_detector(text_to_analyze):
    """
    Detect emotions from the input text using the Watson NLP service.
    Returns a dictionary containing the emotion scores and the dominant emotion.
    """

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, json=input_json, headers=headers)

    # Convert the JSON response into a Python dictionary
    formatted_response = json.loads(response.text)

    # Extract the emotion scores
    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    anger = emotions["anger"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions["sadness"]

    # Find the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Return the required output format
    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion
    }