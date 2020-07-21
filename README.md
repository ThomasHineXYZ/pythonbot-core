# PythonBot-Core

A Python bot that is based off of [BloodyThorn](https://github.com/bloodythorn)'s [WiiHacky](https://github.com/bloodythorn/wiihacky/) project, but slimmed down so that I can learn how to do some proper Python work.

## Requirements
1. An [application and bot setup for Discord](https://discord.com/developers/). You'll need the token for it.
1. a mysql database with login information to log into a db. -> currently
 not used
1. A redis database for the user system. -> currently used.
1. Python 3.7+ installed

## Instructions
1. Clone this repo into the place you want to run it from.
1. Set your Discord token in your environment variables: `DISCORD_BOT_TOKEN=put_your_token_here`
1. Run `pip3 install -r requirements.txt` to install all of the required dependancies.
1. Run the main script: `python3 ./bot`

Currently all configs are saved to redis. No redis access means no persistence in anything.

We're licensed under MIT

## Credits
* [Python Discord Bot](https://github.com/python-discord/bot) where some of the code for this bot was both inspired by and copied from
* [BloodyThorn](https://github.com/bloodythorn) and his [WiiHacky](https://github.com/bloodythorn/wiihacky/) project
