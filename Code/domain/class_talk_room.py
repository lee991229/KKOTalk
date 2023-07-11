
class TalkRoom:
    def __init__(self, talk_room_id, talk_room_name, open_time_stamp):
        self.talk_room_id = talk_room_id
        self.talk_room_name = talk_room_name
        self.open_time_stamp = open_time_stamp

    def __str__(self):
        return f"{self.__repr__()}"

    def __repr__(self):
        return f"{self.__dict__}"
