import socket

from Code.domain.class_user import User


class ClientApp2:
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
        self.client_socket.setblocking(False)
        self.user = None
        self.user_id = None
        self.user_pw = None
        self.user_nickname = None

        # client function =================================

    def send_join_id_for_assert_same_username(self, input_username: str):
        data_msg = input_username.encode(self.FORMAT)
        data_msg_length = len(data_msg)
        request_msg = self.assert_username
        header_msg = f"{request_msg:<{self.HEADER_LENGTH}}{data_msg_length:<{self.HEADER_LENGTH}}".encode(self.FORMAT)
        self.client_socket.send(header_msg + data_msg)  # 헤더를 붙이고 보내는 동작(?)
        return_result = self.client_socket.recv(self.HEADER_LENGTH).decode(self.FORMAT)  # 응답 받기
        print(return_result)
        if return_result == 'pass':
            return True
        elif return_result == '.':
            return False

    def send_join_id_and_pw_for_join_access(self, join_username, join_pw, join_nickname):
        join_user = User(None, join_username, join_pw, join_nickname)
        user_json_str = join_user.toJSON()
        self.client_socket.send(self.HEADER_LIST[self.join_user])
        self.client_socket.recv(self.BUFFER)  # "." 받음
        self.client_socket.send(user_json_str.encode())
        return_result = self.client_socket.recv(self.BUFFER).decode(self.FORMAT)  # 응답 받기
        if return_result == 'pass':
            return True
        elif return_result == '.':
            return False

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
