import os
from dotenv import load_dotenv

from pathlib import Path
from dotenv import load_dotenv

env_path = Path(".") / ".env.debug"

print(env_path)
print('INSIDE GLOBAL')

load_dotenv(dotenv_path=env_path)
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
# print(DISCORD_TOKEN)

SETTINGS_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SETTINGS_PATH)
DATA_DIR = os.path.join(ROOT_DIR,'data')

print(SETTINGS_PATH,ROOT_DIR,DATA_DIR)