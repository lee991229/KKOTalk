import datetime
import socket
import time
from threading import *

from Code.domain.class_message import Message
from Code.domain.class_talk_room import TalkRoom
from Code.domain.class_user import User
from Code.domain.class_user_talk_room import UserTalkRoom
from Common.class_json import KKODecoder


class ClientApp:
    HOST = '127.0.0.1'
    PORT = 9999
    BUFFER = 50000
    FORMAT = "utf-8"
    HEADER_LENGTH = 30

    assert_username = "assert_username"
    join_user = "join_user"
    login = "login"
    enter_square = "enter_square"
    all_user_list = "all_user_list"
    user_talk_room_list = "user_talk_room_list"
    talk_room_user_list_se = 'talk_room_user_list_se'
    out_talk_room = 'out_talk_room'
    send_msg_se = 'send_msg_se'
    invite_user_talk_room = 'invite_user_talk_room'
    make_talk_room = 'make_talk_room'
    talk_room_msg = 'talk_room_msg'
    send_msg_c_room = "send_msg_c_room"
    send_alarm_c_room = "send_alarm_c_room"
    send_ = "send_alarm_c_room"

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
        self.user_id = None
        self.user_pw = None
        self.username = None
        self.user_nickname = None
        self.stored_talk_message = dict()

        self.receive_thread = Thread(target=self.receive_message)
        self.receive_thread.daemon = True
        self.receive_thread.start()
        self.talk_room_list_in_memory = list()
        self.client_widget = None
        self.decoder = KKODecoder()
        self.all_user_list_in_memory = list()
        self.selected_talk_room_id = 1
        self.buffer_guest_list = None

        #

        # client function =================================

    def set_widget(self, widget_):
        self.client_widget = widget_

    def get_user_self(self):
        return User(self.user_id, self.username, self.user_pw, self.user_nickname)

    def get_user_by_id(self, user_id):
        find_list = [x for x in self.all_user_list_in_memory if x.user_id == user_id]
        found_user = find_list[0]
        return found_user

    def get_all_user_list(self):
        return self.all_user_list_in_memory.copy()

    def get_not_yet_invited_user_list(self):
        total_user_list = self.get_all_user_list().copy()
        now_talk_room_id = self.selected_talk_room_id
        talk_room_obj = self.get_talk_room_by_room_id(now_talk_room_id)
        user_list = talk_room_obj.talk_room_user_list.copy()
        result_list = [x for x in total_user_list if x not in user_list]
        for user in result_list:
            print(user.user_id)
        return result_list

    def get_already_invited_user_list(self):
        now_talk_room_id = self.selected_talk_room_id
        talk_room_obj = self.get_talk_room_by_room_id(now_talk_room_id)
        user_list = talk_room_obj.talk_room_user_list.copy()
        return user_list

    def get_talk_room_by_room_id(self, talk_room_id: int):
        assert isinstance(talk_room_id, int)
        result = None
        for talk_room in self.talk_room_list_in_memory:
            temp_num = talk_room.talk_room_id
            if temp_num == talk_room_id:
                result = talk_room
                break
        if result is None:
            raise '결과 찾기 실패'
        found_talk_room = result
        return found_talk_room

    def send_join_id_for_assert_same_username(self, input_username: str):
        data_msg = f"{input_username:<{self.BUFFER - self.HEADER_LENGTH}}".encode(self.FORMAT)
        data_msg_length = len(data_msg)
        request_msg = self.assert_username
        header_msg = f"{request_msg:<{self.HEADER_LENGTH}}".encode(self.FORMAT)
        self.client_socket.send(header_msg + data_msg)  # 헤더를 붙이고 보내는 동작(?)

    def send_join_id_and_pw_for_join_access(self, join_username, join_pw, join_nickname):
        join_user = User(None, join_username, join_pw, join_nickname)
        user_json_str = join_user.toJSON()
        request_msg = self.join_user
        result = self.fixed_volume(request_msg, user_json_str)
        self.client_socket.send(result)

    def send_login_id_and_pw_for_login_access(self, login_username, login_pw):
        # 로그인 파일이 있다고 가정하고 제작
        login_user = User(None, login_username, login_pw, None)
        login_user_str = login_user.toJSON()
        request_msg = self.login
        result = self.fixed_volume(request_msg, login_user_str)
        self.client_socket.send(result)  # 응답 받기

    # 로그인시 가져와야하는 정보들을 한번에 묶을수 있을까? 헤더 그리고 반환값이 달라서 문제임
    def send_enter_square(self):
        user_object = User(self.user_id, self.username, self.user_pw, self.user_nickname)
        user_object_str = user_object.toJSON()
        request_msg = self.enter_square
        result = self.fixed_volume(request_msg, user_object_str)
        self.client_socket.send(result)

    def send_all_user_list(self):
        user_object = User(self.user_id, self.username, self.user_pw, self.user_nickname)
        user_object_str = user_object.toJSON()
        request_msg = self.all_user_list
        result = self.fixed_volume(request_msg, user_object_str)
        self.client_socket.send(result)

    def send_user_talk_room_list(self):
        user_object = User(self.user_id, self.username, self.user_pw, self.user_nickname)
        user_object_str = user_object.toJSON()
        request_msg = self.user_talk_room_list
        result = self.fixed_volume(request_msg, user_object_str)
        self.client_socket.send(result)

    def send_talk_room_user_list_se(self, talk_room_id):
        """
        해당 방 정보 유저 갱신
        :param talk_room_id:
        :return:
        """
        self.selected_talk_room_id = talk_room_id  # 해당 선택된 톡방 저장
        user_talk_room_obj = UserTalkRoom(None, self.user_id, talk_room_id)
        user_talk_room_obj_str = user_talk_room_obj.toJSON()
        request_msg = self.talk_room_user_list_se
        result = self.fixed_volume(request_msg, user_talk_room_obj_str)
        self.client_socket.send(result)

    def send_out_talk_room(self, talk_room_id):
        user_talk_room_obj = UserTalkRoom(None, self.user_id, talk_room_id)
        user_talk_room_obj_str = user_talk_room_obj.toJSON()
        request_msg = self.out_talk_room
        result = self.fixed_volume(request_msg, user_talk_room_obj_str)
        self.client_socket.send(result)

    def send_send_msg_se(self, talk_room_id, msg):
        msg_obj = Message(None, self.user_id, talk_room_id, str(datetime.datetime.now()), msg, None,
                          User(self.user_id, self.username, self.user_pw, self.user_nickname))
        # self.store_message(msg_obj)
        msg_obj_str = msg_obj.toJSON()
        request_msg = self.send_msg_se
        result = self.fixed_volume(request_msg, msg_obj_str)
        self.client_socket.send(result)

    def send_invite_user_talk_room(self, talk_room_id, invite_user):
        user_talk_room_obj = UserTalkRoom(None, invite_user, talk_room_id)
        user_talk_room_obj_str = user_talk_room_obj.toJSON()
        request_msg = self.invite_user_talk_room
        result = self.fixed_volume(request_msg, user_talk_room_obj_str)
        self.client_socket.send(result)

    def send_make_talk_room(self, room_name, guest_user_id_list: list[int], open_time_stamp):
        """2번에 나눠서 로직 구성됨, 1) 방 개설 / 2) 방 입장시키기"""
        self.buffer_guest_list = guest_user_id_list
        create_room = TalkRoom(None, room_name, open_time_stamp)
        create_room_str = create_room.toJSON()
        reqeust_msg = self.make_talk_room
        result = self.fixed_volume(reqeust_msg, create_room_str)
        self.client_socket.send(result)

    def invite_guest_user(self, talk_room_id):
        # 방 아이디를 부여받아야함. talk_room_id 부여 받고 스레드상에서 발동됨
        guest_user_id_list = self.buffer_guest_list
        for guest_id in guest_user_id_list:
            self.send_invite_user_talk_room(talk_room_id, guest_id)
        self.send_talk_room_user_list_se(talk_room_id)
        self.buffer_guest_list.clear()

    def send_talk_room_msg(self, talk_room_id):
        user_talk_room_obj = UserTalkRoom(None, self.user_id, talk_room_id)
        user_talk_room_obj_str = user_talk_room_obj.toJSON()
        reqeust_msg = self.talk_room_msg
        result = self.fixed_volume(reqeust_msg, user_talk_room_obj_str)
        self.client_socket.send(result)

    # 크기 고정으로 만들어 주는 함수
    def fixed_volume(self, header, data):
        header_msg = f"{header:<{self.HEADER_LENGTH}}".encode(self.FORMAT)
        data_msg = f"{data:<{self.BUFFER - self.HEADER_LENGTH}}".encode(self.FORMAT)
        return header_msg + data_msg

    def store_message(self, message_obj):
        """
        클라이언트 stored_talk_message 변수에 메시지를 저장하는 함수
        :param message_obj:
        :return:
        """
        talk_room_id = message_obj.talk_room_id

        if talk_room_id not in self.stored_talk_message.keys():
            self.stored_talk_message.update({talk_room_id: list()})

        target_message_list = self.stored_talk_message[talk_room_id]
        target_message_list.append(message_obj)

    def send_file_to_chat_room(self):
        # todo: send 메시지
        pass

    def receive_message(self):
        while True:
            # self.return_result = self.client_socket.recv(self.BUFFER).decode(self.FORMAT)
            return_result = self.client_socket.recv(self.BUFFER).decode(self.FORMAT)
            response_header = return_result[:self.HEADER_LENGTH].strip()
            response_data = return_result[self.HEADER_LENGTH:].strip()
            print(f"CLIENT RECEIVED: ({response_header},{response_data})")
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
            # 로그인 신청 확인 결과, 로그인한 유저정보 저장?
            elif response_header == self.login:
                if response_data == '.':
                    self.client_widget.log_in_signal.emit(False)
                else:
                    object_data = self.decoder.decode_any(response_data)
                    self.username = object_data.username
                    self.user_id = object_data.user_id
                    self.user_pw = object_data.password
                    self.user_nickname = object_data.nickname
                    self.client_widget.log_in_signal.emit(True)
            # 초기 단톡방 입장 반환
            elif response_header == self.enter_square:
                if response_data == 'pass':
                    self.client_widget.enter_square_signal.emit(True)
            # 본인 제외 모든 유저 정보
            elif response_header == self.all_user_list:
                if response_data == '.':
                    print('오류?')
                else:
                    self.all_user_list_in_memory = self.decoder.decode_any(response_data)
                    self.client_widget.all_user_list_signal.emit(response_data)
            # 채팅방 리스트 정보
            elif response_header == self.user_talk_room_list:
                self.talk_room_list_in_memory = self.decoder.decode_any(response_data)
                for talk_room_obj in self.talk_room_list_in_memory:
                    self.send_talk_room_user_list_se(talk_room_obj.talk_room_id)
                self.client_widget.user_talk_room_signal.emit(response_data)

            # 채팅방 참여 유저 정보
            elif self.talk_room_user_list_se in response_header:
                if response_data == '.':
                    print('아무도 없는 방')
                else:
                    if len(self.talk_room_list_in_memory) == 0:
                        time.sleep(0.05)  # 정보가 받아질 때까지 대기
                    try:

                        header_str, talk_room_id_str = response_header.split("%")
                        print(header_str, talk_room_id_str)
                        talk_room_id = int(talk_room_id_str.strip())
                        self.client_widget.talk_room_user_list_se_signal.emit(talk_room_id, response_data)
                    except:
                        return
            # 방나가기
            elif response_header == self.out_talk_room:
                if response_data == 'pass':
                    self.client_widget.out_talk_room_signal.emit(True)
                elif response_data == '.':
                    self.client_widget.out_talk_room_signal.emit(False)
            # 메시지 받기
            elif response_header == self.send_msg_se:
                msg_obj = self.decoder.decode_any(response_data)
                # if msg_obj.sender_user_id == self.user_id:
                #     pass
                # else:
                #     self.client_widget.send_msg_se_signal.emit(response_data)
                self.client_widget.send_msg_se_signal.emit(response_data)

            # 상대방 초대
            elif response_header == self.invite_user_talk_room:
                if response_data == 'pass':
                    self.client_widget.invite_user_talk_room_signal.emit(True)
                elif response_data == '.':
                    self.client_widget.invite_user_talk_room_signal.emit(False)
            # 방 만들기
            elif response_header == self.make_talk_room:
                talk_room_obj = self.decoder.decode_any(response_data)
                self.invite_guest_user(talk_room_obj.talk_room_id)
                self.talk_room_list_in_memory.append(talk_room_obj)
                self.client_widget.make_talk_room_signal.emit(talk_room_obj.talk_room_id)

            # 메시지 받아보기
            elif response_header == self.talk_room_msg:
                message_list = self.decoder.decode_any(response_data)
                for m in message_list:
                    self.store_message(m)
                self.client_widget.talk_room_msg_signal.emit(response_data)
