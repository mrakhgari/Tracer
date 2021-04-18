from telethon.sync import TelegramClient
from config import *  ## import the user config and details


def get_client(has_proxy=False, proxy_ip="127.0.0.1", proxy_port=1080):
    """

    Create the telegram client. if you want to set socks5 proxy set the has_proxy to true and
    change the port and ip of your proxy.
    """
    proxy = None
    if has_proxy:
        proxy = ("socks5", proxy_ip, proxy_port)

    return TelegramClient(
        username, api_id, api_hash, proxy=("socks5", proxy_ip, proxy_port)
    )
