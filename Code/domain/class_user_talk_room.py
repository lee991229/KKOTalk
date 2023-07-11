
class UserTalkRoom:
    def __init__(self, user_talk_room_id, user_id, talk_room_id):
        self.user_talk_room_id = user_talk_room_id
        self.user_id = user_id
        self.talk_room_id = talk_room_id

    def __str__(self):
        return f"{self.__repr__()}"

    def __repr__(self):
        return f"{self.__dict__}"
