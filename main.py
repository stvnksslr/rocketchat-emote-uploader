import requests
from bs4 import BeautifulSoup
from pathlib import Path

smiley_source = requests.get("https://forums.somethingawful.com/misc.php?action=showsmilies")
soup = BeautifulSoup(smiley_source.content, "html.parser")
emote_folder = Path.cwd() / "emotes"

test = soup.findAll("li", {"class": "smilie"})
list_of_emotes = [smilie.contents for smilie in test]

dict_of_emotes = {}

for emote in list_of_emotes:
    emote_name = emote[3].attrs.get('title')
    emote_url = emote[3].attrs.get('src')
    emote_command = emote[1].text
    dict_of_emotes.update({emote_name: emote_url})

for key, value in dict_of_emotes.items():
    emote = requests.get(value)
    open(emote_folder / key, 'wb').write(emote.content)
