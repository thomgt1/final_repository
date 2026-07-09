"""
Emotion Detector Web Application.
This module provides a Flask web server for emotion detection.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/")
def render_index_page():
    """Render the index page of the Emotion Detector application."""
    return render_template('index.html')


@app.route("/emotionDetector")
def emotion_detector_route():
    """Process the text input and return the emotion detection results."""
    # Get text from URL query param
    text_to_analyze = request.args.get('textToAnalyze')

    # Call emotion detector function
    result = emotion_detector(text_to_analyze)

    # Error handling — if dominant_emotion is None
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Extract scores
    anger_score      = result['anger']
    disgust_score    = result['disgust']
    fear_score       = result['fear']
    joy_score        = result['joy']
    sadness_score    = result['sadness']
    dominant_emotion = result['dominant_emotion']

    # Format and return response
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger_score}, "
        f"'disgust': {disgust_score}, "
        f"'fear': {fear_score}, "
        f"'joy': {joy_score} and "
        f"'sadness': {sadness_score}. "
        f"The dominant emotion is {dominant_emotion}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
