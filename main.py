from os import getenv
from dotenv import load_dotenv
from app.rocketchat_uploader import RocketChat
from argparse import ArgumentParser
from pathlib import Path
from json import loads

# Loads env file might be a better way of doing this
load_dotenv()
default_emote_files_path = 'emote_files/'
rocketchat = RocketChat(api_url=getenv("API_URL"), user_id=getenv("USER_ID"),
                        auth_token=getenv("AUTH_TOKEN"))

parser = ArgumentParser(description='Please Add a file of emotes to be uploaded')
parser.add_argument('--f', type=str, help='File of emotes to be uploaded')
emote_filename = parser.parse_args().f
if emote_filename:
    path_to_files = Path.cwd() / default_emote_files_path / emote_filename
    with open(path_to_files, 'r') as file:
        parsed_emotes_dict = loads(file.read())
    RocketChat.upload_to_rocketchat(item=parsed_emotes_dict)
else:
    print('Please enter valid file name, or make sure your file is in the emote_json folder')
