from telethon.sync import TelegramClient
from telegram_wrapper import get_client, authorization, get_groups_and_channels, get_history_of_entity
import asyncio
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
import json
from message import MessageEncoder

# if you want to use proxy to connect to telegram set the variable as True, otherwise set False.
has_proxy = False

client: TelegramClient = get_client(has_proxy=has_proxy)

client.start()

if not client.is_user_authorized():
    authorization(client)

loop = asyncio.get_event_loop()

# get list of user channels and groups
groups, channels = loop.run_until_complete(get_groups_and_channels(client))

all_info = {}
channels_info = json.loads("[]")
groups_info = json.loads("[]")

for channel in channels:
    entity_info = {}
    channel_message = loop.run_until_complete(
        get_history_of_entity(client, channel))
    entity_info['messages'] = channel_message
    entity_info['id'] = channel.id
    entity_info['title'] = channel.title
    channels_info.append(entity_info)

for group in groups:
    entity_info = {}
    group_message = loop.run_until_complete(
        get_history_of_entity(client, group))
    entity_info['messages'] = group_message
    entity_info['id'] = group.id
    entity_info['title'] = group.title
    groups_info.append(entity_info)

all_info['groups'] = groups_info
all_info['channels'] = channels_info


with open('./../data/corona_data.json', 'w', encoding='utf-8') as f:
    json.dump(all_info, f, ensure_ascii=False, indent=4, cls=MessageEncoder)
