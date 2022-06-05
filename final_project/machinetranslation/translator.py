"""
Translation Class for Watson Translator
"""

import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

class Translator:
    """
    Translator Class.
    Gives the possibility to translate strings from English to French and French to English
    """

    def __init__(self):
        """
        Instantiates a Watson Translator
        """
        load_dotenv()

        apikey = os.environ['apikey']
        url = os.environ['url']

        try:
            self.authenticator = IAMAuthenticator(apikey)
            self.language_translator = LanguageTranslatorV3(
                version='2018-05-01',
                authenticator=self.authenticator
            )
            self.language_translator.set_service_url(url)
        except ApiException as ex:
            print ("Method failed with status code " + str(ex.code) + ": " + ex.message)

    def english_to_french( self, english_text ):
        """
        Translates a given string in English to French
        """
        if english_text == '':
            return ''

        translation_response = self.language_translator.translate(\
            text=english_text, model_id='en-fr')

        french_text=translation_response.get_result()
        # print(french_text['translations'][0]['translation'])
        return french_text['translations'][0]['translation']

    def french_to_english( self, french_text ):
        """
        Translates a given string in French to English
        """
        if french_text == '':
            return ''

        translation_response = self.language_translator.translate(\
            text=french_text, model_id='fr-en')

        english_text=translation_response.get_result()
        # print(english_text['translations'][0]['translation'])
        return english_text['translations'][0]['translation']
