import json


class TalkRoom:
    def __init__(self, talk_room_id, talk_room_name, open_time_stamp):
        self.talk_room_id = talk_room_id
        self.talk_room_name = talk_room_name
        self.open_time_stamp = open_time_stamp

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def __repr__(self):
        return f'{self.__dict__}'

    def __eq__(self, other):
        if isinstance(other, TalkRoom) and \
                self.talk_room_id == other.talk_room_id and \
                self.talk_room_name == other.talk_room_name and \
                self.open_time_stamp == other.open_time_stamp:
            return True
        return False
