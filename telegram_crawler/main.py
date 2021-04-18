from telethon.sync import TelegramClient
from telegram_wrapper import get_client

has_proxy = True  ## if you want to use proxy to connect to telegram set the variable as True, otherwise set False.

client: TelegramClient = get_client()
