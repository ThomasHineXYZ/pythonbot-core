import discord
import discord.ext.commands as disextc
import os
from pathlib import Path
from dotenv import load_dotenv

# Constants

# Load up the environment variables
env_file_name = '.env'
env_path = Path('.') / env_file_name
load_dotenv(dotenv_path=env_path)

# Check if .env.local exists, if so, load up those variables, overriding the
# previously set ones
local_env_file_name = env_file_name + '.local'
local_env_path = Path('.') / local_env_file_name
if os.path.isfile(local_env_file_name):
    load_dotenv(dotenv_path=local_env_path, override=True)

reserved_commands = [
    'giphy', 'tenor', 'tts', 'me', 'tableflip',
    'unflip', 'shrug', 'spoiler'
]

__version__ = 'v0.0.2'
text_wh_version = 'wiihacky_version'
text_wh_name = 'WiiHacks'
id_discord_admin = os.environ['ID_DISCORD_ADMIN']
id_discord_guild = os.environ['ID_DISCORD_GUILD']
id_discord_bot = os.environ['ID_DISCORD_BOT']

reddit_user_role_id = 708924829679747073

moderator_and_up = [
    657740509854302222,
    708923965824827454,
    657743368415215637,
]

health_and_safety_text = """** **
     :warning: WARNING-HEALTH AND SAFETY

BEFORE PLAYING, READ YOUR OPERATIONS
  MANUAL FOR IMPORTANT INFORMATION
      ABOUT YOUR HEALTH AND SAFETY.

                          Also online at
          www.nintendo.com/healthsafety

                     Press Ⓐ to continue.
"""


# Helpers

# TODO: These both need to be replaced by codeblock paginators.
async def paginate(
        message: str,
        pag: disextc.Paginator = None
        ) -> disextc.Paginator:
    """ Helper to use the Paginator.

    Given a line of text it will format it and return the paginator to add
    more lines.

    :param message -> str type with message to send
    :param pag -> Pagenator to add to, or none to create a new.
    :return -> Paginator containing line of text.
    """
    if pag is None:
        pag = disextc.Paginator()
    pag.add_line(message)
    return pag


async def send_paginator(
        to: discord.abc.Messageable,
        pag: disextc.Paginator) -> None:
    """ Helper to send a paginator.

    Given a messageable and a paginator, this function will send the
    paginator the target.

    :param to -> Messageable recipient.
    :param pag -> Pagenator to send.
    :return None
    """
    for page in pag.pages:
        await to.send(page)
