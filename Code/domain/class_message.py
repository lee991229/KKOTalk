import json


class Message:
    def __init__(self, message_id, sender_user_id, talk_room_id, send_time_stamp, contents, long_contents_id, user_obj=None):
        self.message_id = message_id
        self.sender_user_id = sender_user_id
        self.talk_room_id = talk_room_id
        self.send_time_stamp = send_time_stamp
        self.contents = contents
        self.long_contents_id = long_contents_id
        self.user_obj = user_obj

    def toJSON(self):

        obj_str = json.dumps(self, default=lambda o: o.__dict__)
        return obj_str


    def __repr__(self):
        return f'{self.__dict__}'

    def __eq__(self, other):
        if isinstance(other, Message) and \
                self.message_id == other.message_id and \
                self.sender_user_id == other.sender_user_id and \
                self.talk_room_id == other.talk_room_id and \
                self.send_time_stamp == other.send_time_stamp and \
                self.contents == other.contents and \
                self.long_contents_id == other.long_contents_id:
            return True
        return False

