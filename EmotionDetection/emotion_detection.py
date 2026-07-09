import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Send request
    response = requests.post(url, headers=headers, json=input_json)
    
    # Step 1: Handle blank entry — status_code 400
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Step 2: Convert response to dictionary
    response_dict = json.loads(response.text)
    
    # Step 3: Extract emotions
    emotions = response_dict['emotionPredictions'][0]['emotion']
    
    anger_score   = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score    = emotions['fear']
    joy_score     = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Step 4: Find dominant emotion
    emotion_scores = {
        'anger':   anger_score,
        'disgust': disgust_score,
        'fear':    fear_score,
        'joy':     joy_score,
        'sadness': sadness_score
    }
    
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Step 5: Return result
    return {
        'anger':            anger_score,
        'disgust':          disgust_score,
        'fear':             fear_score,
        'joy':              joy_score,
        'sadness':          sadness_score,
        'dominant_emotion': dominant_emotion
    }