from dotenv import load_dotenv
from pathlib import Path
import os

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
