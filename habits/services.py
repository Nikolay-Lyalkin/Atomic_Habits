import os

import requests
from dotenv import load_dotenv

load_dotenv()


def send_telegram_message(chat_id, message):

    url = "https://api.telegram.org"
    TOKEN = os.getenv("TG_API")
    chat_id = chat_id
    message = message
    response = requests.get(f"{url}/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}")
    return response
