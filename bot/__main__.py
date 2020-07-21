from dotenv import load_dotenv
import aiohttp
import discord
import discord.ext.commands as disextc
import logging as lg
import os

from logging import handlers
from pathlib import Path

import cogs

# TODO: Make the log level settable at during runtime.

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

# Set Debug Level: Pull debug mode from env
DEBUG_MODE = None
if 'DEBUG' in os.environ:
    DEBUG_MODE = os.environ['DEBUG']

# Prep Logger
log_level = lg.DEBUG if DEBUG_MODE else lg.INFO
log_format_string = '%(asctime)s | %(name)s | %(levelname)s | %(message)s'
log_format = lg.Formatter(log_format_string)

log_file = Path('logs', 'botlog.log')
log_file.parent.mkdir(exist_ok=True)
log_file_count = 50
max_file_size = 2**16*8*2
file_handler = handlers.RotatingFileHandler(
    log_file,
    maxBytes=max_file_size,
    backupCount=log_file_count,
    encoding='utf-8')
file_handler.setFormatter(log_format)

stream_handler = lg.StreamHandler()
stream_handler.setFormatter(log_format)

log = lg.getLogger()
log.setLevel(log_level)
log.addHandler(file_handler)
log.addHandler(stream_handler)

# Set helper lib libraries log levels.
set_to_warning = ('discord', 'websockets', 'asyncio', 'urllib3.connectionpool',
                  'prawcore', 'aioredis')
for a in set_to_warning:
    lg.getLogger(a).setLevel(lg.WARNING)

log.info('Logger is setup.')

# Module Constants
command_character = os.environ['COMMAND_CHARACTER']
message_cache = 1000 * 10
txt_help_description = \
    """r/WiiHacks Discord Help Menu"""
# todo: move to persona, add more, make rand responder.
txt_activity_name = "with mankind's vulnerabilities"
# txt_activity_name = "Mankind and Plotting its Demise"
txt_activity_state = 'In Development'
txt_activity_details = \
    "First I will start with the weak, while the strong are enslaved."

# Create Bot
wh = disextc.Bot(
    max_messages=message_cache,
    command_prefix=disextc.when_mentioned_or(*command_character),
    fetch_offline_members=True,
    description=txt_help_description,
    activity=discord.Activity(
        name=txt_activity_name,
        type=discord.ActivityType.playing,
        state=txt_activity_state,
        details=txt_activity_details))

# I believe this needs to be here
st = len('cogs.')
module_names = (
    cogs.aliases_mods.__name__[st:],
    cogs.aliases_users.__name__[st:],
    cogs.config.__name__[st:],
    cogs.discord.discord.__name__[st:],
    cogs.discord.synergii.__name__[st:],
    cogs.laboratory.__name__[st:],
    cogs.memory.__name__[st:],
    cogs.persona.__name__[st:],
    cogs.security.__name__[st:],
    cogs.system.__name__[st:])

cog_names = (
    cogs.aliases_mods.ModAliases.__qualname__,
    cogs.aliases_users.UserAliases.__qualname__,
    cogs.config.Config.__qualname__,
    cogs.discord.Discord.__qualname__,
    cogs.discord.Synergii.__qualname__,
    cogs.laboratory.Laboratory.__qualname__,
    cogs.memory.Memory.__qualname__,
    cogs.persona.Persona.__qualname__,
    cogs.security.Security.__qualname__,
    cogs.system.System.__qualname__)

# Load Cog/Extensions
for a in module_names:
    log.info(f'Loading module: {a}')
    wh.load_extension('cogs.' + a)

# TODO: Retry/fail attempts
# Attempt to loin to discord
try:
    log.info('Bot Starting...')

    # Check if the Discord bot token is set or not
    if len(os.environ['DISCORD_BOT_TOKEN']) == 0:
        print("You're missing the DISCORD_BOT_TOKEN env variable in your local file.")
        exit(-1)

    wh.run(os.environ['DISCORD_BOT_TOKEN'])
except KeyError as e:
    log.critical('DISCORD_BOT_TOKEN not set in env.')
    exit(-1)
except discord.errors.LoginFailure as e:
    log.error('Failed to login with given token: {}'.format(e.args))
    exit(-1)
except aiohttp.ClientConnectionError as e:
    log.error(f'Failed to login to discord: {e.args}')
    exit(-1)
except RuntimeError as e:
    log.info('Loop experienced a runtime error: {}'.format(e.args))
    exit(0)
