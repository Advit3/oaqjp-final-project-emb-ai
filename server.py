"""Flask interface and JSON endpoint for emotion detection."""

from flask import Flask, jsonify, render_template, request

from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """Render the input form."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """Analyze the query text and return JSON or a clear validation error."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    if not text_to_analyze.strip():
        return jsonify({"error": "Please enter text to analyze."}), 400

    result = emotion_detector(text_to_analyze)
    if result["dominant_emotion"] is None:
        return jsonify({"error": "Emotion analysis failed for this text."}), 400
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
