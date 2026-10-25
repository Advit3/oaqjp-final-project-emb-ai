"""Unit tests for emotion detection formatting and error paths."""

import unittest
from unittest.mock import Mock, patch

from EmotionDetection.emotion_detection import emotion_detector


class EmotionDetectorTests(unittest.TestCase):
    """Check stable response fields and Watson response handling."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_returns_formatted_prediction(self, post):
        response = Mock()
        response.status_code = 200
        response.json.return_value = {
            "emotionPredictions": [{"emotion": {
                "anger": 0.1, "disgust": 0.05, "fear": 0.05,
                "joy": 0.7, "sadness": 0.1,
            }}]
        }
        post.return_value = response
        result = emotion_detector("I am delighted.")
        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertEqual(result["joy"], 0.7)

    def test_empty_input_returns_none_scores(self):
        result = emotion_detector("  ")
        self.assertIsNone(result["dominant_emotion"])
        self.assertTrue(all(result[key] is None for key in (
            "anger", "disgust", "fear", "joy", "sadness"
        )))

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_http_400_returns_none_scores(self, post):
        response = Mock()
        response.status_code = 400
        post.return_value = response
        result = emotion_detector("bad input")
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
