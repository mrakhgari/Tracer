from telethon.sync import TelegramClient
from telegram_wrapper import get_client, authorization

# if you want to use proxy to connect to telegram set the variable as True, otherwise set False.
has_proxy = True

client: TelegramClient = get_client(has_proxy=has_proxy)

client.start()

if not client.is_user_authorized():
    authorization(client)
