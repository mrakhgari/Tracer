from telethon.sync import TelegramClient
from telegram_wrapper import get_client, authorization, get_groups_and_channels
import asyncio

# if you want to use proxy to connect to telegram set the variable as True, otherwise set False.
has_proxy = True

client: TelegramClient = get_client(has_proxy=has_proxy)

client.start()

if not client.is_user_authorized():
    authorization(client)

loop = asyncio.get_event_loop()
# get list of user channells and groups 
groups, channels = loop.run_until_complete(get_groups_and_channels(client))
