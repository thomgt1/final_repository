"""
Flask application for detecting emotions in user-provided text.
Provides two routes:
- "/" renders the index page.
- "/emotionDetector" processes emotion detection requests.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/")
def render_index_page():
    """
    Render the main index HTML page.

    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET","POST"])
def sent_detector():
    """
    Detect emotions from the provided text query parameter.

    Retrieves the 'textToAnalyze' argument from the request,
    passes it to the emotion detector, formats the response,
    and returns a human-readable output string.

    Returns:
        str: Formatted emotion detection result.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get("textToAnalyze")



    # emotion_detector now returns (emotion_data, status_code)
    emotion_data, status_code = emotion_detector(text_to_analyze)

    # Watson returned 500 or unexpected error
    if status_code == 500 or emotion_data is None:
        return ("Emotion detection service error.", 500)

    # Watson returned 400 → invalid text
    if status_code == 400:
        return ("Emotion detection failed: invalid text.", 400)

    # Normal successful case (status_code == 200)
    emotions = list(emotion_data.items())[:-1]
    formatted_emotions = ", ".join(f"'{key}': {value}" for key, value in emotions)
    dominant_emotion = emotion_data.get("dominant_emotion")

    return (
        f"For the given statement, the system response is {formatted_emotions}. "
        f"The dominant emotion is {dominant_emotion}.",
        200
    )


if __name__ == "__main__":
    # Run the Flask application on host 0.0.0.0 and port 5000
    app.run(host="0.0.0.0", port=5000)
