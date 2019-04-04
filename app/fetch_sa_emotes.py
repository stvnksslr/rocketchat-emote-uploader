from requests import get
from bs4 import BeautifulSoup

parsed_emotes_dict = {}

smiley_source = get(
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
