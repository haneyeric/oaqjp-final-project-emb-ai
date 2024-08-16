from flask import Flask
from EmotionDetection.emotion_detection import emotion_detector
import json
app = Flask(__name__)

@app.route('/emotionDetector/<string:text_to_analyze>')
def detect_emotions(text_to_analyze):
    res = emotion_detector(text_to_analyze)
    dominant_emotion = res.pop('dominant_emotion')
    res_string = str(res)
    res_string = res_string[1:-1]
    mes = "For the given statement, the system response is " + res_string + ". The dominant emotion is " + dominant_emotion + "."


    return {"message": mes}