import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    """
    Unit test class for verifying the accuracy of the emotion detector function
    across different emotional states.
    """

    def test_return_joy(self):
        """Tests if joyous text properly outputs 'joy' as the dominant emotion."""
        response = emotion_detector('I am glad this happened')
        self.assertEqual(response['dominant_emotion'], 'joy')

    def test_return_anger(self):
        """Tests if angry text properly outputs 'anger' as the dominant emotion."""
        response = emotion_detector('I am really mad about this')
        self.assertEqual(response['dominant_emotion'], 'anger')

    def test_return_disgust(self):
        """Tests if disgusted text properly outputs 'disgust' as the dominant emotion."""
        response = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(response['dominant_emotion'], 'disgust')

    def test_return_sadness(self):
        """Tests if sad text properly outputs 'sadness' as the dominant emotion."""
        response = emotion_detector('I am so sad about this')
        self.assertEqual(response['dominant_emotion'], 'sadness')

    def test_return_fear(self):
        """Tests if fearful text properly outputs 'fear' as the dominant emotion."""
        response = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(response['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
