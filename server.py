"""
Flask application for detecting emotions in user-provided text.
Provides two routes:
- "/" renders the index page.
- "/emotionDetector" processes emotion detection requests.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/", methods=["GET"])
def render_index_page():
    """
    Render the main index HTML page.

    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET", "POST"])
def sent_detector():
    """
    Detect emotions from the provided text query parameter.

    Retrieves the 'textToAnalyze' argument from the request,
    sends it to the Watson emotion detector, and returns a formatted
    response string along with the appropriate HTTP status code.

    Returns:
        tuple: (formatted response string, HTTP status code)
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get("textToAnalyze")

    # Call the emotion detector, which returns (emotion_data, status_code)
    emotion_data, status_code = emotion_detector(text_to_analyze)

    # Handle Watson API failure or missing dominant emotion
    if status_code == 400 and emotion_data.get("dominant_emotion") is None:
        return "Invalid input! Try again."

    # Handle Watson API 400 response (invalid text)
    if status_code == 400:
        # Extract all emotion scores except the dominant emotion
        emotions = list(emotion_data.items())[:-1]

        # Format emotion scores into a readable string
        formatted_emotions = ", ".join(f"'{key}': {value}" for key, value in emotions)

        # Extract the dominant emotion (always None for 400)
        dominant_emotion = emotion_data.get("dominant_emotion")

        # Return formatted output with HTTP 400 status
        return (
            f"For the given statement, the system response is {formatted_emotions}. "
            f"The dominant emotion is {dominant_emotion}."
        )

    # Normal successful case (status_code == 200)
    # Extract all emotion scores except the dominant emotion
    emotions = list(emotion_data.items())[:-1]

    # Format emotion scores into a readable string
    formatted_emotions = ", ".join(f"'{key}': {value}" for key, value in emotions)

    # Extract the dominant emotion
    dominant_emotion = emotion_data.get("dominant_emotion")

    # Return formatted output with HTTP 200 status
    return (
        f"For the given statement, the system response is {formatted_emotions}. "
        f"The dominant emotion is {dominant_emotion}.",
        200
    )


if __name__ == "__main__":
    # Run the Flask application on host 0.0.0.0 and port 5000
    app.run(host="0.0.0.0", port=5000)
