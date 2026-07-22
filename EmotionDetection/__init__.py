"""
EmotionDetection Package
This package provides emotion detection functionality using Watson NLP library
"""

# Import the emotion_detector function from the emotion_detection module
from .emotion_detection import emotion_detector

# Define what gets imported with "from EmotionDetection import *"
__all__ = ['emotion_detector']