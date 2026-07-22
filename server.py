"""
Emotion Detection Web Application
Flask server that provides emotion detection functionality via web interface
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the index.html template for the root URL
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detector_endpoint():
    """
    Handle emotion detection requests via GET and POST methods
    
    Returns:
        str: Formatted emotion analysis result or error message
    """
    if request.method == 'GET':
        # Get the text to analyze from the query parameters
        text_to_analyze = request.args.get('textToAnalyze')
    else:
        # Get the text to analyze from the form data
        text_to_analyze = request.form.get('textToAnalyze')
    
    # Check if text was provided
    if not text_to_analyze or text_to_analyze.strip() == '':
        return "Invalid text! Please try again!"
    
    try:
        # Call the emotion detection function
        result = emotion_detector(text_to_analyze)
        
        # Check if there was an error in the result
        if 'error' in result:
            return f"Error analyzing text: {result['error']}"
        
        # Check if dominant_emotion is None (invalid input)
        if result['dominant_emotion'] is None:
            return "Invalid text! Please try again!"
        
        # Format the output as specified
        response = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']:.9f}, "
            f"'disgust': {result['disgust']:.10f}, "
            f"'fear': {result['fear']:.9f}, "
            f"'joy': {result['joy']:.7f} and "
            f"'sadness': {result['sadness']:.9f}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )
        
        return response
        
    except Exception as e:
        # Handle any unexpected errors
        return f"An error occurred during emotion detection: {str(e)}"

@app.errorhandler(404)
def page_not_found(error):
    """
    Handle 404 errors
    """
    return render_template('index.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors
    """
    return "Internal server error occurred. Please try again later.", 500

if __name__ == '__main__':
    # Run the Flask application on localhost:5000
    app.run(host='0.0.0.0', port=5000, debug=True)