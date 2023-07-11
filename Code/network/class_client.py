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
        self.client = socket(AF_INET, SOCK_STREAM)
        # 아직 쓴 이유를 모르겠음 일단 필요할것 같음
        self.connect_to_surver()
        # 임의로 지정
        self.user_id = 'test1'
        self.user_pw = 'password'
        self.validate_user(self.user_id, self.user_pw)



    def set_config(self, configure):
        print('클라이언트 설정 적용됨')

    # 소캣이 서버에 접촉
    def connect_to_surver(self):
        self.client.connect(self.SERVER)

    def validate_user(self, user_id, user_pw):
        client = self.client
        format_ = self.FORMAT
        buffer = self.BUFFER
        # 아이디 전송
        client.send(user_id.encode(format_))
        if client.recv(buffer).decode(format_) == '아이디존재':
            # 비밀번호 전송
            client.send(user_pw.encode(format_))
            if client.recv(buffer).decode(format_) == "연결됨":
                # 연결상태로 변경
                self.connected = True
                print('도착')
                self.send_thread = Thread(target=self.send_message)
                self.send_thread.start()
                self.receive_thread = Thread(target=self.receive_message)
                self.receive_thread.start()
                while True:
                    pass
                # 화면 변경되면서 채팅바응로 들어가진다.

            # 로그인되면 크크오톡 화면 뜨는건가? UI뜨게 변경되는 느낌인가?
            # self.receive_thread.start()

    def send_message(self):
        while True:
            # 메시지 전송
            message = input()
            self.client.send(message.encode(self.FORMAT))
            # 보내진 아이디 받기
            message = self.client.recv(self.BUFFER).decode(self.FORMAT)
            print(message)

    def receive_message(self):
        while self.connected:
            message = self.client.recv(self.BUFFER).decode(self.FORMAT)
            print(message)

    def start(self):
        print(f'클라이언트 프로그램 가동 시작 : {datetime.datetime.now()}')

    def exit(self):
        print(f'클라이언트 프로그램 종료 시작 : {datetime.datetime.now()}')
