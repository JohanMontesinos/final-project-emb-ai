"""
Emotion Detection of a given text using
IBM Watson NLP API
"""

import json

import requests


def emotion_detector(text_to_analyze):
    """
    Function to detect the emotion of a given text using IBM Watson NLP API.
    :param text_to_analyze: Text input for emotion detection
    :return: Dictionary containing the detected emotions and their scores
    """
    # Defining IBM Watson NLP API endpoint for emotion detection request
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyze}}
    # Making a POST request to the IBM Watson NLP API for emotion detection
    response = requests.post(url, headers=headers, json=myobj, timeout=9)
    # Parsing the response to json for extracting the emotion scores
    response_dict = json.loads(response.text)
    emotions = response_dict["emotionPredictions"][0]["emotion"]
    anger_score = emotions["anger"]
    disgust_score = emotions["disgust"]
    fear_score = emotions["fear"]
    joy_score = emotions["joy"]
    sadness_score = emotions["sadness"]
    # Determining the dominant emotion based on the highest score
    dominant_emotion = max(emotions, key=emotions.get)
    # Creating a dictionary to store the emotion scores and the dominant emotion
    output = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion,
    }
    # Returning the output dictionary containing the emotion scores and dominant emotion
    return output
