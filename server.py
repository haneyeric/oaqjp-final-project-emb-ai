"""Module running server for emotion dtector"""
from flask import Flask
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector/<string:text_to_analyze>')
def detect_emotions(text_to_analyze):
    """Handler for detct emotions API."""
    res = emotion_detector(text_to_analyze)
    dominant_emotion = res.pop('dominant_emotion')
    if dominant_emotion is None:
        return {"message": "Invalid text! Please try again!"}
    res_string = str(res)
    res_string = res_string[1:-1]
    mes = "For the given statement, the system response is "
    mes += res_string + ". The dominant emotion is " + dominant_emotion + "."


    return {"message": mes}
