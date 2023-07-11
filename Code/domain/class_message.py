class Message:
    def __init__(self, message_id, sender_user_id, talk_room_id, contents, send_time_stamp, long_contents_id):
        self.message_id = message_id
        self.sender_user_id = sender_user_id
        self.talk_room_id = talk_room_id
        self.contents = contents
        self.send_time_stamp = send_time_stamp
        self.long_contents_id = long_contents_id