"""
This module initiates the Flask web application for emotion detection.
It routes requests to the frontend and processes text via the emotion detector.
"""
from flask import Flask, render_template, request
from emotion_detection import emotion_detector

# Module-level variables must be UPPER_CASE to comply with PyLint constants rules
APP = Flask('My App')

@APP.route('/')
def render_emotion_detector():
    """
    Renders the main application index HTML page.
    """
    return render_template('index.html')

@APP.route('/emotionDetector')
def emotion_detector_call():
    """
    Retrieves text from the request arguments, passes it to the
    emotion detector function, and handles 400 errors if the text is invalid.
    """
    # Variable names must use snake_case instead of camelCase
    text_to_analyze = request.args.get('textToAnalyze', '')
    response = emotion_detector(text_to_analyze)

    # Verifies if the response dictionary has a dominant_emotion of None
    if isinstance(response, dict) and response.get('dominant_emotion') is None:
        return "Invalid text! Please try again!", 400

    return response

if __name__ == '__main__':
    APP.run(debug=True)
