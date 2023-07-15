
import json

from Code.domain.class_long_contents import LongContents
from Code.domain.class_message import Message
from Code.domain.class_talk_room import TalkRoom
from Code.domain.class_user import User
from json import JSONEncoder, JSONDecoder

from Code.domain.class_user_talk_room import UserTalkRoom



class KKOEncoder(JSONEncoder):

    def __init__(self):
        super().__init__()


    def encode(self, o) -> str:
        if isinstance(o, list) and isinstance(o[0], User):
            temp_list = list()
            for obj in o:
                str_obj = obj.toJSON()
                temp_list.append(str_obj)
            return json.dumps(temp_list)

        elif isinstance(o, list) and isinstance(o[0], Message):
            temp_list = list()
            for obj in o:
                str_obj = obj.toJSON()
                temp_list.append(str_obj)
            return json.dumps(temp_list)

        return json.dumps(o, default=lambda o: o.__dict__)


    def default(self, o):
        return o.__dict__


class KKODecoder(JSONDecoder):
    def __init__(self):
        super().__init__()

    def decode_any(self, o):
        o: str
        if o.startswith("["):  # list type
            list_type_obj = json.loads(o)
            temp_list = list()
            for obj in list_type_obj:
                one_obj = self.decode_obj(obj)
                temp_list.append(one_obj)
            return temp_list

        else:
            print(o)
            return self.decode_obj(o)

    def decode_obj(self, o):
        try:
            dict_obj = self.decode(o)
        except Exception:
            dict_obj = o
        if 'user_talk_room_id' in dict_obj.keys():
            return UserTalkRoom(dict_obj['user_talk_room_id'], dict_obj['user_id'], dict_obj['talk_room_id'])
        elif 'user_id' in dict_obj.keys():
            return User(dict_obj['user_id'], dict_obj['username'], dict_obj['password'], dict_obj['nickname'])
        elif 'message_id' in dict_obj.keys():
            temp_user = User(*dict_obj['user_obj'].values())
            return Message(dict_obj['message_id'], dict_obj['sender_user_id'], dict_obj['talk_room_id'],
                           dict_obj['send_time_stamp'], dict_obj['contents'], dict_obj['long_contents_id'], temp_user)
        elif 'talk_room_id' in dict_obj.keys():
            return TalkRoom(dict_obj['talk_room_id'], dict_obj['talk_room_name'], dict_obj['open_time_stamp'])
        elif 'contents_id' in dict_obj.keys():
            return LongContents(dict_obj['contents_id'], dict_obj['contents_type'], dict_obj['long_text'],
                                dict_obj['image'])


if __name__ == '__main__':
    encoder = KKOEncoder()
    decoder = KKODecoder()
    user1 = User(1, '짱구', '12345', '짱구닉네임')
    user2 = User(2, '철수', '12345', '철수닉네임')
    user3 = User(3, '훈이', '12345', '훈이닉네임')
    user4 = User(4, '유리', '12345', '유리닉네임')
    user5 = User(5, '맹구', '12345', '맹구닉네임')
    user6 = User(6, '수지', '11111', '수지닉네임')
    user7 = User(7, '치타', '11111', '치타닉네임')
    usertalkroom1 = UserTalkRoom(1, 1, 1)
    usertalkroom2 = UserTalkRoom(2, 1, 2)
    usertalkroom3 = UserTalkRoom(3, 4, 2)
    usertalkroom4 = UserTalkRoom(4, 2, 3)
    usertalkroom5 = UserTalkRoom(5, 1, 4)
    usertalkroom6 = UserTalkRoom(6, 6, 4)
    usertalkroom7 = UserTalkRoom(7, 7, 4)
    talkroom1 = TalkRoom(1, '1번방', '2023-01-01 00:00:00')
    talkroom2 = TalkRoom(2, '2번방', '2023-02-01')
    talkroom3 = TalkRoom(3, '3번방', '2023-03-01')
    talkroom4 = TalkRoom(4, '4번방', '2023-04-01')
    message1 = Message(1, user4.user_id, 2, '2020-01-01', '호롤로 메시지 내용', None, user1)
    message2 = Message(2, user4.user_id, 2, '2020-01-01', None, 1)
    message3 = Message(3, user1.user_id, 3, '2020-01-01', None, 2)
    message4 = Message(4, user2.user_id, 1, '2020-01-01', None, 3)
    message5 = Message(4, user5.user_id, 3, '2020-01-01', None, 4)
    long1 = LongContents(1, 0, long_text='아주 긴 글1', image=None)  # 타입일치
    long2 = LongContents(2, 1, long_text='아주 긴 글2', image=None)  # 불일치
    long3 = LongContents(3, 0, long_text=None, image='사진3')  # 불일치
    long4 = LongContents(4, 1, long_text=None, image='사진4')  # 타입일치

    obj_1 = encoder.encode(user1)
    obj_2 = encoder.encode(usertalkroom1)
    obj_3 = encoder.encode(talkroom1)
    obj_4 = encoder.encode(message1)
    obj_5 = encoder.encode(long1)

    obj_decoded1 = decoder.decode(obj_1)
    obj_decoded2 = decoder.decode(obj_2)
    obj_decoded3 = decoder.decode(obj_3)
    obj_decoded4 = decoder.decode(obj_4)
    obj_decoded5 = decoder.decode(obj_5)
    # print(obj_1)
    # print(obj_2)
    # print(obj_3)
    # print(obj_4)
    # print(obj_5)
    # print(obj_decoded1)
    # print(obj_decoded2)
    # print(obj_decoded3)
    # print(obj_decoded4)
    # print(obj_decoded5)
    # print(type(obj_decoded1))
    # print(type(obj_decoded2))
    # print(type(obj_decoded3))
    # print(type(obj_decoded4))
    # print(type(obj_decoded5))

    user_list = [
        user1,
        user2,
        user3,
        user4,
        user5,
        user6,
        user7
    ]
    list_str_obj = encoder.encode(user_list)
    # print(type(list_str_obj))
    list_obj = decoder.decode_any(list_str_obj)
    print(type(list_obj))
    print(type(list_obj[0]))

