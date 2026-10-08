import json
import requests
def emotion_detector(text_to_analyse):
    # URL for emotional detector API 
    url = ('https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict')
    # Header
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Payload
    myobj = {"raw_document": {"text": text_to_analyse}}
    # Post to the API
    response = requests.post(url, json=myobj, headers=header)
    
    # Convert into a dictionary using json
    # formatted_response = json.loads(response)
    formatted_response = response.json()
    # Extract the emotion dictionary from the first prediction
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    # Extract individual scores
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    #
    # Determine the dominant emotion (highest score)
    dominant_emotion = max(emotions, key=emotions.get)
    #
    return {
    'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score,
    'dominant_emotion': dominant_emotion
    }
