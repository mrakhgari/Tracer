from telethon.sync import TelegramClient
from config import *  # import the user config and details
from message import Message

def get_client(has_proxy=False, proxy_ip="127.0.0.1", proxy_port=1080):
    """

    Create the telegram client. if you want to set socks5 proxy set the has_proxy to true and
    change the port and ip of your proxy.
    """
    proxy = None
    if has_proxy:
        proxy = ("socks5", proxy_ip, proxy_port)

    return TelegramClient(
        username, api_id, api_hash, proxy=proxy
    )


def authorization(client: TelegramClient):
    client.send_code_request(phone)
    try:
        client.sign_in(phone, input('Enter the code: '))
    except SessionPasswordNeededError:
        client.sign_in(password=input('Password: '))


async def get_groups_and_channels(client: TelegramClient):
    groups, channels = [], []

    async for dialog in client.iter_dialogs():
        if dialog.is_group:
            groups.append(dialog)
        elif dialog.is_channel:
            channels.append(dialog)
    return groups, channels

async def get_history_of_entity(client, chat):
    messages = []

    async for message in client.iter_messages(chat, wait_time=0):
        if has_date_limit and message.date < date_limit:
            break
        messages.append(Message(message))
    return messages