"""
Emotion Detection Module
This module provides emotion detection functionality using Watson NLP library
"""

import requests
import json

def emotion_detector(text_to_analyze):
    """
    Detect emotions from the given text using Watson NLP Emotion Predict function
    
    Args:
        text_to_analyze (str): The text to be analyzed for emotions
    
    Returns:
        dict: Dictionary containing emotion scores and dominant emotion
    """
    # Define the URL and headers for the Emotion Predict function
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Prepare the input JSON
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    try:
        # Make the POST request to the emotion detection API
        response = requests.post(url, json=input_json, headers=headers)
        
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f01e2ba (Added error handling for blank input and invalid text)
        # Check if the status code is 400 (Bad Request - empty or invalid input)
        if response.status_code == 400:
            # Return dictionary with all values as None for invalid input
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        
<<<<<<< HEAD
=======
>>>>>>> d26be9e (Added EmotionDetection package with __init__.py)
=======
>>>>>>> f01e2ba (Added error handling for blank input and invalid text)
        # Convert the response text to a dictionary
        response_dict = json.loads(response.text)
        
        # Extract the emotion predictions from the response
        emotion_predictions = response_dict.get('emotionPredictions', [])
        
        if emotion_predictions:
            # Get the first prediction (assuming only one document was sent)
            emotions = emotion_predictions[0].get('emotion', {})
            
            # Extract the required emotions with default values if missing
            anger_score = emotions.get('anger', 0.0)
            disgust_score = emotions.get('disgust', 0.0)
            fear_score = emotions.get('fear', 0.0)
            joy_score = emotions.get('joy', 0.0)
            sadness_score = emotions.get('sadness', 0.0)
            
            # Create a dictionary of emotion scores for finding the dominant emotion
            emotion_scores = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
            }
            
            # Find the dominant emotion (emotion with highest score)
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)
            
            # Return the formatted output
            return {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }
        else:
            # Return default values if no emotion predictions found
            return {
                'anger': 0.0,
                'disgust': 0.0,
                'fear': 0.0,
                'joy': 0.0,
                'sadness': 0.0,
                'dominant_emotion': None
            }
            
    except requests.exceptions.RequestException as e:
        # Handle any request errors
        return {
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f01e2ba (Added error handling for blank input and invalid text)
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
<<<<<<< HEAD
=======
            'anger': 0.0,
            'disgust': 0.0,
            'fear': 0.0,
            'joy': 0.0,
            'sadness': 0.0,
>>>>>>> d26be9e (Added EmotionDetection package with __init__.py)
=======
>>>>>>> f01e2ba (Added error handling for blank input and invalid text)
            'dominant_emotion': None,
            'error': str(e)
        }
    except json.JSONDecodeError as e:
        # Handle JSON parsing errors
        return {
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f01e2ba (Added error handling for blank input and invalid text)
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
<<<<<<< HEAD
=======
            'anger': 0.0,
            'disgust': 0.0,
            'fear': 0.0,
            'joy': 0.0,
            'sadness': 0.0,
>>>>>>> d26be9e (Added EmotionDetection package with __init__.py)
=======
>>>>>>> f01e2ba (Added error handling for blank input and invalid text)
            'dominant_emotion': None,
            'error': f"JSON parsing error: {str(e)}"
        }