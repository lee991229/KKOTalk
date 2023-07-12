import os
from multiprocessing import Process
from socket import *
from threading import Thread, Event

import select


class Server2:
    HOST = '127.0.0.1'
    PORT = 9999
    BUFFER = 1024
    FORMAT = "utf-8"
    HEADER_LENGTH = 16

    assert_username = "assert_username"
    join_user = "join_user"
    login = "login"
    send_msg_c_room = "send_msg_c_room"
    send_alarm_c_room = "send_alarm_c_room"
    pass_encoded = f"{'pass':<{HEADER_LENGTH}}".encode(FORMAT)
    dot_encoded = f"{'.':<{HEADER_LENGTH}}".encode(FORMAT)

    HEADER_LIST = {
        assert_username: assert_username.encode(FORMAT),
        join_user: join_user.encode(FORMAT),
        login: login.encode(FORMAT),
        send_msg_c_room: send_msg_c_room.encode(FORMAT),
        send_alarm_c_room: send_alarm_c_room.encode(FORMAT),
    }

    def __init__(self, db_conn):
        # 서버 소켓 설정
        self.db_conn = db_conn
        self.server_socket = None
        self.config = None
        self.sockets_list = list()
        self.clients = dict()
        self.thread_for_run = None
        self.run_signal = True

    def set_config(self, configure):
        self.config = configure
        print('서버 설정 적용됨')

    def start(self):
        if self.thread_for_run is not None:  # 실행중이면 종료 시키기
            return
        self.server_socket = socket(AF_INET, SOCK_STREAM)  # AF_INET(ipv4를 의미)
        self.server_socket.bind((self.HOST, self.PORT))  # 바인딩
        self.server_socket.listen()  # 리슨 시작
        self.sockets_list.clear()  # 소켓리스트 클리어
        self.sockets_list.append(self.server_socket)
        self.run_signal = True
        self.thread_for_run = Thread(target=self.run)
        self.thread_for_run.start()

    def stop(self):
        self.run_signal = False
        if self.thread_for_run is not None:
            self.thread_for_run.join()
        self.server_socket.close()
        self.thread_for_run = None

    def run(self):
        while True:
            if self.run_signal is False:
                break
            try:
                read_sockets, _, exception_sockets = select.select(self.sockets_list, [], self.sockets_list, 0.1)
            except Exception:
                continue
            for notified_socket in read_sockets:
                print(notified_socket)
                if notified_socket == self.server_socket:
                    client_socket, client_address = self.server_socket.accept()
                    user = self.receive_message(client_socket)
                    print(user)
                    if user is False:
                        continue
                    self.sockets_list.append(client_socket)
                    self.clients[client_socket] = user

                else:
                    message = self.receive_message(notified_socket)

                    if message is False:
                        self.sockets_list.remove(notified_socket)
                        del self.clients[notified_socket]
                        continue


            for notified_socket in exception_sockets:
                self.sockets_list.remove(notified_socket)
                del self.clients[notified_socket]

    def receive_message(self, client_socket:socket):
        try:
            message_header = client_socket.recv(self.HEADER_LENGTH*2)
            request_msg = message_header[:self.HEADER_LENGTH].strip().decode(self.FORMAT)
            data_length = int(message_header[self.HEADER_LENGTH:].strip().decode(self.FORMAT))
            input_data = client_socket.recv(data_length).decode(self.FORMAT)
            print(f"message_header : {message_header}")
            print(f"request_msg : {request_msg}")
            print(f"data_length : {data_length}")
            print(f"input_data : {input_data}")
            if request_msg == self.assert_username:
                client_socket.send(self.pass_encoded)
                data_msg = client_socket.recv(data_length).decode(self.FORMAT)
                print(f"클라이언트로 받은 요청 : {request_msg} | 내용 : {data_msg}")
                return {'header': message_header, 'data': client_socket.recv(data_length)}
        except:
            return False

    # def listening(self):
    #     while True:
    #         msg = self.server.recv(1024).decode("utf-8")
    #         if msg == '/assert_username':
    #             self.server.send(self.ENCODED_DOT)
    #             response = self.server.recv(1024).decode("utf-8")
    #             if self.db_conn.assert_same_join_id(response) is True:
    #                 self.server.send(self.ENCODED_PASS)
    #             else:
    #                 self.server.send('.'.encode())
    #         elif msg == '/join_user':
    #             self.server.send(self.ENCODED_DOT)
    #             response = self.server.recv(1024).decode("utf-8")
    #             if self.join_access(response) is True:
    #                 self.server.send('pass'.encode(encoding='utf-8'))
    #             else:
    #                 self.server.send(self.ENCODED_PASS)
    #         elif msg == '/login':
    #             self.server.send(self.ENCODED_DOT)
    #             response = self.server.recv(1024).decode("utf-8")
    #             if self.join_access(response) is True:
    #                 self.server.send(self.ENCODED_PASS)
    #             else:
    #                 self.server.send(self.ENCODED_DOT)
    #
    # def assert_same_join_id(self, input_username):
    #     return self.db_conn.assert_same_login_id(input_username)
    #
    # def join_access(self, join_user_json_str: str):
    #     join_user_obj = self.decoder.decode(join_user_json_str)
    #     join_user_obj: User
    #     if self.db_conn.insert_user(join_user_obj) is not False:
    #         print(f"유저 {join_user_obj.nickname} 가입 성공")
    #         return True
    #     else:
    #         return False
    #
    # def login_access(self, login_message: str):
    #     username, pw = login_message.split('%')
    #     if self.db_conn.user_log_in(username, pw):
    #         print(f"유저 {username} 로그인 성공")
    #         return True
    #     else:
    #         return False
