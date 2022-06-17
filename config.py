import os
import logging


BACKEND = 'Telegram'  
BOT_IDENTITY = {"token": os.getenv("TELEGRAM_TOKEN")}
BOT_DATA_DIR = r'/err/data'
BOT_EXTRA_PLUGIN_DIR = r'/err/plugins'
BOT_EXTRA_BACKEND_DIR = r'/err/local_backends'
BOT_PREFIX = "/"
BOT_ALT_PREFIXES = ("Bot",)
BOT_ALT_PREFIX_SEPARATORS = (",",)

BOT_LOG_FILE = r'/err/errbot.log'
BOT_LOG_LEVEL = logging.DEBUG


BOT_ADMINS = (os.getenv("TELEGRAM_ID"),)