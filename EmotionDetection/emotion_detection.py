"""Call Watson NLP and normalize emotion prediction results."""

import requests

WATSON_URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
MODEL_ID = "emotion_aggregated-workflow_lang_en_stock"
EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def _empty_result():
    """Return the stable response shape used for invalid input/errors."""
    result = {emotion: None for emotion in EMOTIONS}
    result["dominant_emotion"] = None
    return result


def emotion_detector(text_to_analyze):
    """Analyze text and return five scores plus the dominant emotion.

    An empty string or an HTTP 400 response returns all emotion fields as None.
    """
    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return _empty_result()

    headers = {"grpc-metadata-mm-model-id": MODEL_ID}
    payload = {"raw_document": {"text": text_to_analyze}}
    try:
        response = requests.post(
            WATSON_URL, json=payload, headers=headers, timeout=15
        )
    except requests.RequestException:
        return _empty_result()

    if response.status_code == 400:
        return _empty_result()
    response.raise_for_status()
    prediction = response.json()["emotionPredictions"][0]["emotion"]
    result = {emotion: prediction[emotion] for emotion in EMOTIONS}
    result["dominant_emotion"] = max(
        EMOTIONS, key=lambda emotion: result[emotion]
    )
    return result
