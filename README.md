# rocketchat-emoji-uploader
emote scraper and uploader for rocketchat

#### Requirements
* python 3.7
* pipenv

##### Notes
* Rocketchat by default has an incredibly low rate limit something like 10 emoji's per minute, if you are doing any kinda batch uploading you are going to want to up this limit for the duration fot he test.
* To upload emoji's via the rest API we are using https://github.com/RocketChat/Rocket.Chat/pull/13160/files#diff-fb50a4cb9f2dd591ac952500ada21a52R34
it is not really documented well but works.
* this project is aimed at the something awful emoji page but at some point in the future i can make it more generic to accept yaml or json lists of emoji names + urls