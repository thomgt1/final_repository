"""
Unit tests for the emotion_detector function.

This module validates that the emotion detection logic correctly identifies
the dominant emotion for a variety of input sentences.
"""

import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Unit test suite for the emotion_detector function."""

    def test_emotion_detector(self):
        """
        Test dominant emotion classification for multiple emotional inputs.
        Each assertion checks whether the returned dominant emotion matches
        the expected label.
        """

        # Positive sentiment: expecting 'joy'
        result_joy = emotion_detector("I am glad this happened")
        self.assertEqual(result_joy["dominant_emotion"], "joy")

        # Anger sentiment: expecting 'anger'
        result_anger = emotion_detector("I am really mad about this")
        self.assertEqual(result_anger["dominant_emotion"], "anger")

        # Disgust sentiment: expecting 'disgust'
        result_disgust = emotion_detector(
            "I feel disgusted just hearing about this"
        )
        self.assertEqual(result_disgust["dominant_emotion"], "disgust")

        # Sadness sentiment: expecting 'sadness'
        result_sadness = emotion_detector("I am so sad about this")
        self.assertEqual(result_sadness["dominant_emotion"], "sadness")

        # Fear sentiment: expecting 'fear'
        result_fear = emotion_detector(
            "I am really afraid that this will happen"
        )
        self.assertEqual(result_fear["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()
