import os

import requests
from dotenv import load_dotenv


load_dotenv()

EVOLUTION_API_URL = os.getenv('EVOLUTION_API_URL')
EVOLUTION_INSTANCE_NAME = os.getenv('EVOLUTION_INSTANCE_NAME')
EVOLUTION_AUTHENTICATION_API_KEY = os.getenv('EVOLUTION_AUTHENTICATION_API_KEY')

class EvolutionApi:

    def __init__(self):
        pass

    def send_message(self, number, text):
        url = f'{EVOLUTION_API_URL}/message/sendText/{EVOLUTION_INSTANCE_NAME}'
        headers = {
            'apikey': EVOLUTION_AUTHENTICATION_API_KEY,
            'Content-Type': 'application/json'
        }
        payload = {
            'number': number,
            'text': text,
        }
        return requests.post(
            url=url,
            json=payload,
            headers=headers,
        ).text
