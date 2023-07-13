import socket
from threading import *
from Code.domain.class_user import User


class ClientApp:
    HOST = '127.0.0.1'
    PORT = 9999
    BUFFER = 1024
    FORMAT = "utf-8"
    HEADER_LENGTH = 30


    assert_username = "assert_username"
    join_user = "join_user"
    login = "login"
    send_msg_c_room = "send_msg_c_room"
    send_alarm_c_room = "send_alarm_c_room"

    HEADER_LIST = {
        assert_username: assert_username.encode(FORMAT),
        join_user: join_user.encode(FORMAT),
        login: login.encode(FORMAT),
        send_msg_c_room: send_msg_c_room.encode(FORMAT),
        send_alarm_c_room: send_alarm_c_room.encode(FORMAT),
    }

    def __init__(self):
        # 서버 소켓 설정
        self.client_socket = None
        self.config = None
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.HOST, self.PORT))
        # self.client_socket.setblocking(False)
        self.user = None
        self.user_id = None
        self.user_pw = None
        self.user_nickname = None
        self.receive_thread = Thread(target=self.receive_message)
        self.receive_thread.start()
        self.client_widget = None

        # client function =================================

    def set_widget(self, widget_):
        self.client_widget = widget_

    def send_join_id_for_assert_same_username(self, input_username: str):
        data_msg = f"{input_username:<{self.BUFFER-self.HEADER_LENGTH}}".encode(self.FORMAT)
        request_msg = self.assert_username
        header_msg = f"{request_msg:<{self.HEADER_LENGTH}}".encode(self.FORMAT)
        self.client_socket.send(header_msg + data_msg)  # 헤더를 붙이고 보내는 동작(?)

    def send_join_id_and_pw_for_join_access(self, join_username, join_pw, join_nickname):
        join_user = User(None, join_username, join_pw, join_nickname)
        user_json_str = join_user.toJSON()
        data_msg = f"{user_json_str:<{self.BUFFER-self.HEADER_LENGTH}}".encode(self.FORMAT)
        request_msg = self.join_user
        header_msg = f"{request_msg:<{self.HEADER_LENGTH}}".encode(self.FORMAT)
        self.client_socket.send(header_msg + data_msg)

    def send_login_id_and_pw_for_login_access(self, login_username, login_pw):
        sending_message = login_username + '%' + login_pw
        self.client_socket.send(self.HEADER_LIST[self.login])
        self.client_socket.recv(self.BUFFER)  # "." 받음
        self.client_socket.send(sending_message.encode())
        return_result = self.client_socket.recv(self.BUFFER).decode(self.FORMAT)  # 응답 받기
        if return_result == 'pass':
            return True
        elif return_result == '.':
            return False

    def send_message_to_chat_room(self):
        # todo: send 메시지
        pass

    def send_file_to_chat_room(self):
        # todo: send 메시지
        pass

    def receive_message(self):
        while True:
            # self.return_result = self.client_socket.recv(self.BUFFER).decode(self.FORMAT)
            return_result = self.client_socket.recv(self.BUFFER).decode(self.FORMAT)
            response_header = return_result[:self.HEADER_LENGTH].strip()
            print(response_header)
            response_data = return_result[self.HEADER_LENGTH:].strip()
            # 아이디 중복 확인 결과
            if response_header == self.assert_username:
                if response_data == 'pass':
                    self.client_widget.assert_same_id_signal.emit(True)
                elif response_data == '.':
                    self.client_widget.assert_same_id_signal.emit(False)
            # 회원 가입 중복 확인 결과
            elif response_header == self.join_user:
                if response_data == 'pass':
                    self.client_widget.sign_up_signal.emit(True)
                elif response_data == '.':
                    self.client_widget.sign_up_signal.emit(False)
                