from dataclasses import dataclass
import requests


@dataclass
class RocketChat:
    api_url: str
    user_id: str
    auth_token: str

    @property
    def emoji_create_url(self):
        return '%s/emoji-custom.create' % self.api_url

    @property
    def auth_headers(self):
        return {
            "X-Auth-Token": self.auth_token,
            "X-User-Id": self.user_id,
            "cache-control": "no-cache",
        }

    def upload_emote(self, emote_name, emote_url, emote_alias):
        try:
            emote_data = dict(name=emote_name)
            if emote_alias and emote_alias != emote_name:
                emote_data['alias'] = emote_alias

            emote_image_data = requests.get(emote_url).content

            response = requests.post(
                self.emoji_create_url,
                headers=self.auth_headers,
                files=dict(
                    emoji=emote_image_data
                ),
                data=emote_data)

            if response.status_code == 200:
                print('created emote: :%s:' % emote_name)
            else:
                print('error creating emote: :%s:' % emote_name)
                print('ERROR: {}'.format(response))
        except Exception:
            raise
