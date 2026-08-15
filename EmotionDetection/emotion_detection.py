import json
import requests

def emotion_detector(text_to_analyze):
    """
    Sends a POST request to the Watson NLP Emotion Predict service,
    parses the JSON response, extracts specific emotion scores,
    finds the dominant emotion, and returns the formatted dictionary.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Send POST request
    response = requests.post(url, json=payload, headers=headers)
    
    # Convert response text into dictionary using json library
    formatted_response = json.loads(response.text)
    
    # Extract the emotion dictionary
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Find dominant emotion (the emotion with highest score)
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Return formatted result
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }