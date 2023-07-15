import sys

from Code.domain.class_db_connector import DBConnector
from Code.domain.class_user_talk_room import UserTalkRoom
from Code.network.class_server import Server
from Common.common_module import *
from Code.domain.class_user import User
from Code.domain.class_talk_room import TalkRoom


if __name__ == '__main__':
    conn = DBConnector()
    conn.create_tables()
    talkroom_1 = TalkRoom(None, 'room1', '1237')
    talkroom_2 = TalkRoom(None, 'room2', '1237')
    talkroom_3 = TalkRoom(None, 'room3', '1237')
    talkroom_4 = TalkRoom(None, 'room4', '1237')
    talkroom_1 = conn.insert_talk_room(talkroom_1)
    talkroom_2 = conn.insert_talk_room(talkroom_2)
    talkroom_3 = conn.insert_talk_room(talkroom_3)
    talkroom_4 = conn.insert_talk_room(talkroom_4)

    user_a = User(None, '1', '123', '뿡뿡이')
    user_b = User(None, '2', '123', '짱구')
    user_c = User(None, '3', '123', '란타로')
    user_d = User(None, '4', '123', '나루토')
    user_e = User(None, '5', '123', '사스케')
    user_f = User(None, '6', '123', '루피')
    user_g = User(None, '7', '123', '이동녘')
    user_h = User(None, '8', '123', '도라에몽')
    user_i = User(None, '9', '123', '지우')
    user_j = User(None, '10', '123', '붓다')
    user_k = User(None, '11', '123', '예수')
    user_l = User(None, '12', '123', '간디')
    user_m = User(None, '13', '123', '보노보노')
    user_n = User(None, '14', '123', '마루코')
    user_o = User(None, '15', '123', '햄토리')
    user_p = User(None, '16', '123', 'love')
    user_a = conn.insert_user(user_a)
    user_b = conn.insert_user(user_b)
    user_c = conn.insert_user(user_c)
    user_d = conn.insert_user(user_d)
    user_e = conn.insert_user(user_e)
    user_f = conn.insert_user(user_f)
    user_g = conn.insert_user(user_g)
    user_h = conn.insert_user(user_h)
    user_i = conn.insert_user(user_i)
    user_j = conn.insert_user(user_j)
    user_k = conn.insert_user(user_k)
    user_l = conn.insert_user(user_l)
    user_m = conn.insert_user(user_m)
    user_n = conn.insert_user(user_n)
    user_o = conn.insert_user(user_o)
    user_p = conn.insert_user(user_p)

    conn.insert_user_talk_room(UserTalkRoom(None, 1, 1))
    conn.insert_user_talk_room(UserTalkRoom(None, 1, 2))
    conn.insert_user_talk_room(UserTalkRoom(None, 1, 3))
    conn.insert_user_talk_room(UserTalkRoom(None, 2, 1))
    conn.insert_user_talk_room(UserTalkRoom(None, 3, 1))
    conn.insert_user_talk_room(UserTalkRoom(None, 4, 1))
    conn.insert_user_talk_room(UserTalkRoom(None, 5, 1))
    conn.insert_user_talk_room(UserTalkRoom(None, 2, 2))
    conn.insert_user_talk_room(UserTalkRoom(None, 3, 2))

    server = Server(conn)
    server.start()
