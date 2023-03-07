"""Module to translate text between english and french"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3 (version='2018-05-01', authenticator= authenticator)
language_translator.set_service_url(url)

def english_to_french(english_text):
    """Function to translate from english to french"""
    if english_text in ('', None):
        return "No text as input"
    french_text = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    #print(json.dumps(frenchText, indent=2, ensure_ascii=False))
    return french_text['translations'][0]['translation']


def french_to_english(french_text):
    """Function to translate from french to english"""
    if french_text in ('', None):
        return "No text as input"
    english_text = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    #print(json.dumps(english_text, indent=2, ensure_ascii=False))
    return english_text['translations'][0]['translation']


def list_languages():
    """Function to see languages available"""
    languages = language_translator.list_languages().get_result()
    print(json.dumps(languages, indent=2))


if __name__ == "__main__":
    result = english_to_french('Hello my friend')
    print(f"result = {result}")
