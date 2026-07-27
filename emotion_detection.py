import json
import requests


def emotion_detector(text_to_analyze):
    # Target URL for the Watson NLP Emotion Predict service
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    # Required headers specifying the model ID
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # JSON payload structure expected by the service
    myobj = {"raw_document": {"text": text_to_analyze}}

    # Send POST request to the Watson NLP Emotion Detection service
    response = requests.post(url, json=myobj, headers=headers)

    # Convert response text into a dictionary using json.loads
    formatted_response = json.loads(response.text)

    # Extract the dictionary containing individual emotion scores
    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    # Extract scores for specific emotions
    anger_score = emotions["anger"]
    disgust_score = emotions["disgust"]
    fear_score = emotions["fear"]
    joy_score = emotions["joy"]
    sadness_score = emotions["sadness"]

    # Determine the dominant emotion (emotion with the maximum score)
    dominant_emotion = max(emotions, key=emotions.get)

    # Return output in requested dictionary format
    return {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion,
    }
