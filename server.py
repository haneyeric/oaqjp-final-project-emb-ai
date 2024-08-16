from flask import Flask
from EmotionDetection.emotion_detection import emotion_detector
import json
app = Flask(__name__)

@app.route('/emotionDetector/<string:text_to_analyze>')
def detect_emotions(text_to_analyze):
    res = emotion_detector(text_to_analyze)
    return {"message": json.dumps(res)}