import requests
from bs4 import BeautifulSoup
from rq import Queue
from redis import Redis
from app.rocketchat import RocketChat

rocketchat = RocketChat(api_url='', user_id='', auth_token='')
redis_conn = Redis()
q = Queue('emotes', connection=redis_conn)
parsed_emotes_dict = {}

smiley_source = requests.get(
    "https://forums.somethingawful.com/misc.php?action=showsmilies")
soup = BeautifulSoup(smiley_source.content, "html.parser")

all_classes_with_emotes = soup.findAll("li", {"class": "smilie"})
list_of_emotes = [emote.contents for emote in all_classes_with_emotes]


def create_dict_of_emotes(item):
    for emote in item:
        emote_name = emote[3].attrs.get('title')
        emote_url = emote[3].attrs.get('src')
        emote_command = emote[1].text
        emote_meta = [emote_command, emote_url]
        parsed_emotes_dict.update({emote_name: emote_meta})


def load_into_que(item):
    for emote_name, meta in item.items():
        emote_alias = meta[0]
        emote_url = meta[1]
        rocketchat.upload_emote(emote_name, emote_url, emote_alias)


create_dict_of_emotes(item=list_of_emotes)
load_into_que(item=parsed_emotes_dict)
