# rocketchat-emoji-uploader
[![Build Status](https://drone.stvnksslr.com/api/badges/stvnksslr/rocketchat-emote-uploader/status.svg)](https://drone.stvnksslr.com/stvnksslr/rocketchat-emote-uploader)
[![Maintainability](https://api.codeclimate.com/v1/badges/21ff237d3f752bb8c72c/maintainability)](https://codeclimate.com/github/stvnksslr/rocketchat-emote-uploader/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/21ff237d3f752bb8c72c/test_coverage)](https://codeclimate.com/github/stvnksslr/rocketchat-emote-uploader/test_coverage)

emote scraper and uploader for rocketchat


#### Requirements
* python 3.7
* pipenv

##### Notes
* Rocketchat by default has an low rate limit of 10 calls per endpoint per minute, if you are doing any kinda batch uploading you are going to want to up this limit for the duration of the upload. Set it to something suitable for your environment:
  * `Administration -> Rate Limit -> API Rate Limit Default number calls to the rate limiter = 10000`
* To upload emoji's via the rest API we are using https://github.com/RocketChat/Rocket.Chat/pull/13160/files#diff-fb50a4cb9f2dd591ac952500ada21a52R34
it is not really documented well but works.
* this project is aimed at the something awful emoji page but at some point in the future i can make it more generic to accept yaml or json lists of emoji names + urls
