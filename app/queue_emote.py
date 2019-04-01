from pathlib import Path

import requests

emote_folder = Path.cwd() / "emotes"


def save_emote(name, value_url, value_command):
    try:
        emote_content = requests.get(value_url).content
        requests.post()
    except Exception:
        raise
