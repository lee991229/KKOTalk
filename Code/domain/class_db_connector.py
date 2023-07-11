import sqlite3

from class_user import User
from class_user_talk_room import UserTalkRoom
from class_talk_room import TalkRoom
from class_message import Message
from class_long_contents import LongContents


class DBConnector:
    _instance = None

    def __new__(cls, test_option=None):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, test_option=None):
        self.conn = None
        self.test_option = test_option

    def start_conn(self):
        if self.test_option is True:
            self.conn = sqlite3.connect('db_test.db')

        else:
            self.conn = sqlite3.connect('main_db.db')
        return self.conn.cursor()

    def end_conn(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None

    def commit_db(self):
        if self.conn is not None:
            self.conn.commit()
        else:
            raise f"cannot commit database! {self.__name__}"

    ## CREATE TABLES ======================================================================= ##
    def create_tables(self):
        c = self.start_conn()
        c.executescript("""
            DROP TABLE IF EXISTS user;
            CREATE TABLE "user" (
                "user_id"	INTEGER,
                "username"	TEXT NOT NULL UNIQUE,  
                "password"	TEXT NOT NULL,
                "nickname"	TEXT NOT NULL,
                PRIMARY KEY("user_id" AUTOINCREMENT)
            );
            DROP TABLE IF EXISTS user_talk_room;
            CREATE TABLE "user_talk_room" (
                "user_talk_room_id"	INTEGER,
                "user_id" INTEGER,
                "talk_room_id"	INTEGER,
                PRIMARY KEY("user_talk_room_id" AUTOINCREMENT)
            );
            DROP TABLE IF EXISTS talk_room;
            CREATE TABLE "talk_room" (
                "talk_room_id"	INTEGER,
                "talk_room_name" TEXT NOT NULL,
                "open_time_stamp"	TEXT NOT NULL,
                PRIMARY KEY("talk_room_id" AUTOINCREMENT)
            );
            DROP TABLE IF EXISTS message;
            CREATE TABLE "message" (
                "message_id" INTEGER, 
                "sender_user_id" INTEGER, 
                "talk_room_id" INTEGER,
                "contents" TEXT, 
                "send_time_stamp" TEXT, 
                "long_contents_id" INTEGER,
                PRIMARY KEY("message_id" AUTOINCREMENT)
            );
            DROP TABLE IF EXISTS long_contents;
            CREATE TABLE "long_contents" (
                "contents_id" INTEGER, 
                "type" INTEGER, 
                "long_text" TEXT, 
                "image" BLOB,
                PRIMARY KEY("contents_id" AUTOINCREMENT)
            );

        """)
        self.commit_db()
        self.end_conn()

    # user 테이블========================================================================================
    def insert_user(self, user_object: User):
        c = self.start_conn()
        user_id = user_object.user_id
        user_name = user_object.username
        password = user_object.password
        nickname = user_object.nickname
        user_id_list = list()
        user_ids = c.execute('select user_id from user').fetchall()
        for _id in user_ids:
            user_id_list.append(_id[0])
        if user_id in user_id_list:
            pass
        else:
            c.execute('insert into user(username, password, nickname) values (?, ?, ?)',
                      (user_name, password, nickname))
            self.commit_db()
            self.end_conn()

    def update_user(self, user_object: User):
        c = self.start_conn()
        user_id = user_object.user_id
        user_name = user_object.username
        password = user_object.password
        nickname = user_object.nickname
        c.execute('update user set username=?, password = ?, nickname=? where user_id = ?',
                  (user_name, password, nickname, user_id))
        self.commit_db()
        self.end_conn()

    def find_all_user(self):
        c = self.start_conn()
        user_data = c.execute('select * from user').fetchall()
        if user_data is None:
            return None
        all_user_obj_list = list()
        for row_user in user_data:
            all_user_obj_list.append(User(*row_user))
        self.end_conn()
        return all_user_obj_list

    def find_user_by_username(self, username):
        c = self.start_conn()
        user_data = c.execute('select * from user where username = ?', (username,)).fetchone()
        if user_data is None:
            return None
        user_object = User(*user_data)
        self.end_conn()
        return user_object

    def delete_user_by_username(self, username: str):
        c = self.start_conn()
        c.execute('delete from user where username = ?', (username,))
        self.commit_db()
        self.end_conn()

    # user_talk_room================================================
    # 새로운 채팅방 생성 함수 호출 및 user_talk_room 테이블 정보 추가
    def insert_user_talk_room(self, user_id, talk_room_name, open_time_stamp):
        talk_room_obj = self.create_talk_room(talk_room_name, open_time_stamp)
        c = self.start_conn()
        talk_room_id = talk_room_obj.talk_room_id
        c.execute('insert into user_talk_room (user_id, talk_room_id) values (?, ?)', (user_id, talk_room_id))
        self.commit_db()
        self.end_conn()

    # 유저가 속한 모든 채팅방 객체 반환
    def find_all_talk_room_by_user_id(self, user_id: int) -> TalkRoom:
        c = self.start_conn()
        users_talk_room_list = list()
        user_talk_rooms = c.execute('select * from user_talk_room where user_id = ?', (user_id,)).fetchall()
        # talk_rooms = c.execute('select * from talk_room').fetchall()
        for user_talk_row in user_talk_rooms:
            user_talk_room_obj = UserTalkRoom(*user_talk_row)
            searched_talk_room = self.find_talk_room_by_id(user_talk_room_obj)
            users_talk_room_list.append(searched_talk_room)
        self.end_conn()
        return users_talk_room_list

    # talk_room_id에 해당하는 톡방에 있는 유저 객체 반환
    def find_all_user_by_talk_id(self, talk_room_id: int):
        c = self.start_conn()
        involved_user = c.execute('select * from user_talk_room where talk_room_id = ?', (talk_room_id,))

        self.end_conn()

    # talk_room 테이블=======================================================
    # 새로운 채팅방 생성
    def create_talk_room(self, talk_room_name, open_time_stamp):
        c = self.start_conn()
        c.execute('insert into talk_room (talk_room_name, open_time_stamp) values (?, ?)',
                  (talk_room_name, open_time_stamp))
        self.commit_db()
        created_talk_room = c.execute('select * from talk_room order by talk_room_id desc limit 1').fetchone()
        created_talk_room_obj = self.find_talk_room_by_id(created_talk_room[0])
        self.end_conn()
        return created_talk_room_obj

    def find_talk_room_by_id(self, user_talk_room_obj: UserTalkRoom):
        c = self.start_conn()
        talk_room_id = user_talk_room_obj.talk_room_id
        row_data = c.execute('select * from talk_room where talk_room_id = ?', (talk_room_id,)).fetchone()
        talk_room_obj = TalkRoom(*row_data)
        self.end_conn()
        return talk_room_obj

    # Message테이블===================================================================================


if __name__ == '__main__':
    dbconn = DBConnector()
    dbconn.create_tables()