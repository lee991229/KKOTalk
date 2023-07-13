from Code.domain.class_message import Message
from Code.domain.class_user import User
from json import JSONEncoder, JSONDecoder


class KKOEncoder(JSONEncoder):

    def __init__(self):
        super().__init__()

    def default(self, o):
        return o.__dict__


class KKODecoder(JSONDecoder):
    def __init__(self):
        super().__init__()

    def decode(self, o, **kwargs):

        dict_obj = super().decode(o, **kwargs)
        if 'user_id' in dict_obj.keys():
            return User(dict_obj['user_id'], dict_obj['username'], dict_obj['password'], dict_obj['nickname'])
        elif 'message_id' in dict_obj.keys():
            return Message(dict_obj['message_id'], dict_obj['sender_user_id'], dict_obj['talk_room_id'],
                           dict_obj['contents'], dict_obj['send_time_stamp'], dict_obj['long_contents_id'])
