import os
import time
from dotenv import load_dotenv

import requests
from bs4 import BeautifulSoup
from app.rocketchat_uploader import RocketChat

load_dotenv()

rocketchat = RocketChat(api_url=os.getenv("API_URL"), user_id=os.getenv("USER_ID"),
                        auth_token=os.getenv("AUTH_TOKEN"))

parsed_emotes_dict = {}


def upload_to_rocketchat(item):
    for emote_name, meta in item.items():
        emote_alias = meta[0]
        emote_url = meta[1]
        time.sleep(.5)
        if len(emote_alias) > 1:
            emote_alias = emote_alias[1:-1]
        rocketchat.upload_emote(emote_alias, emote_url, emote_alias)


upload_to_rocketchat(item=parsed_emotes_dict)
