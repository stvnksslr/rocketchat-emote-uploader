from pathlib import Path
from requests import get, request

emote_folder = Path.cwd() / "emotes"
url = "https://attention.deficit.dev/api/v1/emoji-custom.create"

headers = {
    'X-Auth-Token': "",
    'X-User-Id': "",
    'cache-control': "no-cache",
}


def save_emote(name, value_url, value_command):
    try:
        querystring = {"name": name}
        emote_content = get(value_url).content
        request("POST", url, files=dict(emoji=emote_content), headers=headers, params=querystring)
    except Exception:
        raise
