import json


class UserTalkRoom:
    def __init__(self, user_talk_room_id, user_id, talk_room_id):
        self.user_talk_room_id = user_talk_room_id
        self.user_id = user_id
        self.talk_room_id = talk_room_id


    def __str__(self):
        return f"{self.__repr__()}"

    def __repr__(self):
        return f"{self.__dict__}"

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def __eq__(self, other):
        if isinstance(other, UserTalkRoom) and \
                self.user_talk_room_id == other.user_talk_room_id and \
                self.user_id == other.user_id and \
                self.talk_room_id == other.talk_room_id:
            return True
        return False
