import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers=headers, json=json)
    emotionsResponse = response.json()
    if response.status_code == 200:
        emotions = emotionsResponse['emotionPredictions'][0]['emotion']
        emotions['dominant_emotion'] = max(emotions, key = emotions.get)
    else:
        emotions = {
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion": None
        }
    return emotions
