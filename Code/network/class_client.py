import datetime
import threading
from socket import *
from threading import *


class ClientApp:
    HOST = '127.0.0.1'
    PORT = 9999
    BUFFER = 1024
    FORMAT = "utf-8"
    SERVER = (HOST, PORT)

    def __init__(self):
        # self.controller =  ClientController()
        self.connected = False
        self.message = None
        # 아직 쓴 이유를 모르겠음 일단 필요할것 같음
        # 임의로 지정
        # self.validate_user(self.user_id, self.user_pw)

    def set_config(self, configure):
        print('클라이언트 설정 적용됨')

    # 소캣이 서버에 접촉
    def connect_to_surver(self):
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect(self.SERVER)

    def disconnect_to_surver(self):
        self.client.shutdown(1)
        self.client.close()
        print('죽음?')

    # 프로토 타입에서 로그인 가능함... 지워도 될듯하다.
    def validate_user(self, sending_login):
        client = self.client
        format_ = self.FORMAT
        buffer = self.BUFFER
        # 아이디, 비밀번호
        client.send(sending_login.encode(format_))
        if client.recv(buffer).decode(format_) == 'pass':
            # 연결상태로 변경
            self.connected = True
            self.send_thread = Thread(target=self.send_message)
            self.send_thread.start()
            self.receive_thread = Thread(target=self.receive_message)
            self.receive_thread.start()
            while True:
                pass
        else:
            self.connected = False

    def test_start(self):
        self.receive_thread = Thread(target=self.receive_message)
        self.receive_thread.start()

    def send_message(self):
        while True:
            # 메시지 전송
            message = input()
            self.client.send(message.encode(self.FORMAT))
            # 보내진 아이디 받기
            message = self.client.recv(self.BUFFER).decode(self.FORMAT)
            print(message)

    def receive_message(self):
        while True:
            self.message = self.client.recv(self.BUFFER).decode(self.FORMAT)


    def start(self):
        print(f'클라이언트 프로그램 가동 시작 : {datetime.datetime.now()}')

    def exit(self):
        print(f'클라이언트 프로그램 종료 시작 : {datetime.datetime.now()}')
