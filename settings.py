import os

DEBUG = os.getenv('DEBUG',False)

if DEBUG:
    print('WE are in DEBUG')
    from pathlib import Path
    from dotenv import load_dotenv

    env_path = Path(".") / ".env.debug"
    load_dotenv(dotenv_path=env_path)

    from settings_file.development import *
else:
    print("We are in Production")
    from settings_file.production import *
    