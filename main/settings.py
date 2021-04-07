import os

DEBUG = os.getenv('DEBUG',False)

if DEBUG:
    from settings_file.development import *
else:
    from settings_file.production import *
    