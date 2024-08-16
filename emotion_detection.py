import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    head = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_obj = { "raw_document": { "text": text_to_analyze } }

    res = requests.post(url, json = input_obj, headers = head)

    return res.text