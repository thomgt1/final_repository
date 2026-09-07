"""
Flask application for detecting emotions in user-provided text.
Provides two routes:
- "/" renders the index page.
- "/emotionDetector" processes emotion detection requests.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/", methods=["GET",])
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

    # Run the emotion detector on the provided text
    emotion_data, status_code = emotion_detector(text_to_analyze)


    if status_code == 500 or emotion_data is None:
        return "Invalid input! Try again."

    if status_code == 400:
       # Extract all emotion scores except the dominant emotion
        emotions = list(emotion_data.items())[:-1]

        # Format emotion scores into a readable string
        formatted_emotions = ", ".join(f"'{key}': {value}" for key, value in emotions)

        # Extract the dominant emotion from the response
        dominant_emotion = emotion_data.get("dominant_emotion")

        # Return a formatted string with the detected emotions
        return (
            f"For the given statement, the system response is {formatted_emotions}. "
            f"The dominant emotion is {dominant_emotion}."
        )

    else:
        # Extract all emotion scores except the dominant emotion
        emotions = list(emotion_data.items())[:-1]

        # Format emotion scores into a readable string
        formatted_emotions = ", ".join(f"'{key}': {value}" for key, value in emotions)

        # Extract the dominant emotion from the response
        dominant_emotion = emotion_data.get("dominant_emotion")



        # Return a formatted string with the detected emotions
        return (
            f"For the given statement, the system response is {formatted_emotions}. "
            f"The dominant emotion is {dominant_emotion}."
        )


if __name__ == "__main__":
    # Run the Flask application on host 0.0.0.0 and port 5000
    app.run(host="0.0.0.0", port=5000)
