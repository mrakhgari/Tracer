from telethon.utils import get_peer_id
from json import JSONEncoder


class Message:
    # def __init__(self, id, message, sender_id, date, reply_to, is_user, is_channel, is_bot):
    def __init__(self, message):
        self.id = message.id
        self.message = message.message
        self.is_channel = message.post
        if not self.is_channel and message.from_id is not None:
            # sender_id is id of auther
            self.sender_id = get_peer_id(message.from_id)
        else:
            # sender_id in channels is the channel id
            self.sender_id = get_peer_id(message.peer_id)
        self.date = message.date
        self.reply_to = message.reply_to
        self.entities = message.entities

    def get_sender_id(self, message, chat):
        if from_id is None:  # is channel
            self.is_channel = True
            return chat.id
        else:
            self.is_user = True
            pass

    # def __repr__(self):
        # return self.__str__()

    def __str__(self):
        return f'''
        id: {self.id},
        message: {self.message},
        is_Channel: {self.is_channel},
        sender: {self.sender_id},
        date: {self.date},
        reply_to : {self.reply_to}
        '''

import datetime
class MessageEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.date):
            # return dict(timestamp=o.timestamp)
            return o.strftime("%Y-%m-%dT%H:%M:%S")
            # return dict(year=o.year, month=o.month, day=o.day)
        return o.__dict__
