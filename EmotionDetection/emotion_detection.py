import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    head = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_obj = { "raw_document": { "text": text_to_analyze } }

    res = requests.post(url, json = input_obj, headers = head)
    res_dict = json.loads(res.text)
    emotion_dict = res_dict["emotionPredictions"][0]["emotion"]
    dominant_emotion = ""
    max_emotion = 0

    for key in emotion_dict:
        if emotion_dict[key] > max_emotion:
            max_emotion = emotion_dict[key]
            dominant_emotion = key
    
    emotion_dict['dominant_emotion'] = dominant_emotion

    return emotion_dict